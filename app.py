import os
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from config import config
from models import db, Concurso
from scraper import scrape_pci_concursos

app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_ENV', 'development')])
db.init_app(app)

REGIONS = {
    'nacional': 'Nacional',
    'sudeste': 'Sudeste',
    'sul': 'Sul',
    'norte': 'Norte',
    'nordeste': 'Nordeste',
    'centrooeste': 'Centro-Oeste',
    'ultimas': 'Últimas'
}

STATUS_CHOICES = [
    'Ainda não classificados',
    'Vou ver de novo',
    'Tire da minha lista'
]

@app.route('/')
def index():
    return render_template('index.html', regions=REGIONS, status_choices=STATUS_CHOICES)

@app.route('/api/concursos')
def get_concursos():
    filters = {
        'status': request.args.get('status'),
        'region': request.args.get('region'),
        'uf': request.args.get('uf'),
        'search': request.args.get('search'),
        'hide_removed': request.args.get('hide_removed') == 'true'
    }

    query = Concurso.query

    if filters['status']:
        query = query.filter_by(status=filters['status'])

    if filters['region']:
        query = query.filter_by(regiao=filters['region'])

    if filters['uf']:
        query = query.filter_by(uf=filters['uf'])

    if filters['hide_removed']:
        query = query.filter(Concurso.status != 'Tire da minha lista')

    if filters['search']:
        search = f"%{filters['search']}%"
        query = query.filter(
            (Concurso.titulo.ilike(search)) |
            (Concurso.orgao.ilike(search)) |
            (Concurso.uf.ilike(search))
        )

    concursos = query.order_by(Concurso.data_encontrado.desc()).all()

    return jsonify([{
        'id': c.id,
        'titulo': c.titulo,
        'orgao': c.orgao,
        'uf': c.uf,
        'regiao': c.regiao,
        'link': c.link,
        'cargos': c.cargos,
        'escolaridade': c.escolaridade,
        'vagas': c.vagas,
        'prazo': c.prazo,
        'status': c.status,
        'notas': c.notas,
        'data_encontrado': c.data_encontrado.isoformat() if c.data_encontrado else None,
        'data_atualizacao': c.data_atualizacao.isoformat() if c.data_atualizacao else None
    } for c in concursos])

@app.route('/api/concursos/<int:concurso_id>/status', methods=['PUT'])
def update_status(concurso_id):
    data = request.get_json()
    concurso = Concurso.query.get(concurso_id)

    if not concurso:
        return jsonify({'error': 'Concurso não encontrado'}), 404

    if 'status' in data and data['status'] in STATUS_CHOICES:
        concurso.status = data['status']
        concurso.data_atualizacao = datetime.now()
        db.session.commit()
        return jsonify({'success': True, 'status': concurso.status})

    return jsonify({'error': 'Status inválido'}), 400

@app.route('/api/concursos/<int:concurso_id>/notas', methods=['PUT'])
def update_notas(concurso_id):
    data = request.get_json()
    concurso = Concurso.query.get(concurso_id)

    if not concurso:
        return jsonify({'error': 'Concurso não encontrado'}), 404

    concurso.notas = data.get('notas', '')
    concurso.data_atualizacao = datetime.now()
    db.session.commit()
    return jsonify({'success': True, 'notas': concurso.notas})

@app.route('/api/scrape', methods=['POST'])
def scrape():
    try:
        result = scrape_pci_concursos(db, Concurso)
        return jsonify({
            'success': True,
            'novos': result['novos'],
            'atualizados': result['atualizados'],
            'total': result['total'],
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats')
def get_stats():
    with app.app_context():
        total = db.session.query(func.count(Concurso.id)).scalar()
        por_status = {}
        for status in STATUS_CHOICES:
            count = db.session.query(func.count(Concurso.id)).filter_by(status=status).scalar()
            por_status[status] = count

        por_regiao = {}
        for regiao_key, regiao_label in REGIONS.items():
            count = db.session.query(func.count(Concurso.id)).filter_by(regiao=regiao_key).scalar()
            por_regiao[regiao_label] = count

        return jsonify({
            'total': total,
            'por_status': por_status,
            'por_regiao': por_regiao
        })

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
