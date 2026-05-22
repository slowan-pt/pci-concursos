import os
import requests as _requests
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from bs4 import BeautifulSoup
from config import config
from models import db, Concurso
from scraper import scrape_pci_concursos

_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9',
}

app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_ENV', 'development')])
db.init_app(app)

REGIONS = {
    'nacional':    'Nacional',
    'sudeste':     'Sudeste',
    'sul':         'Sul',
    'norte':       'Norte',
    'nordeste':    'Nordeste',
    'centrooeste': 'Centro-Oeste',
    'ultimas':     'Últimas',
}

STATUS_CHOICES = [
    'Ainda não classificados',
    'Vou ver de novo',
    'Tire da minha lista',
]

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html', regions=REGIONS, status_choices=STATUS_CHOICES)

@app.route('/api/concursos')
def get_concursos():
    status   = request.args.get('status')
    region   = request.args.get('region')
    uf       = request.args.get('uf')
    search   = request.args.get('search')
    hide_rem = request.args.get('hide_removed') == 'true'

    query = Concurso.query

    if status:
        query = query.filter_by(status=status)
    if region:
        query = query.filter_by(regiao=region)
    if uf:
        query = query.filter_by(uf=uf)
    if hide_rem:
        query = query.filter(Concurso.status != 'Tire da minha lista')
    if search:
        s = f"%{search}%"
        query = query.filter(
            Concurso.titulo.ilike(s) |
            Concurso.uf.ilike(s) |
            Concurso.cargos.ilike(s)
        )

    concursos = query.order_by(Concurso.data_encontrado.desc()).all()
    return jsonify([c.to_dict() for c in concursos])

@app.route('/api/concursos/<int:cid>/status', methods=['PUT'])
def update_status(cid):
    data = request.get_json() or {}
    c = db.session.get(Concurso, cid)
    if not c:
        return jsonify({'error': 'Não encontrado'}), 404
    novo = data.get('status')
    if novo not in STATUS_CHOICES:
        return jsonify({'error': 'Status inválido'}), 400
    c.status = novo
    c.data_atualizacao = datetime.now()
    db.session.commit()
    return jsonify({'success': True, 'status': c.status})

@app.route('/api/concursos/<int:cid>/notas', methods=['PUT'])
def update_notas(cid):
    data = request.get_json() or {}
    c = db.session.get(Concurso, cid)
    if not c:
        return jsonify({'error': 'Não encontrado'}), 404
    c.notas = data.get('notas', '')
    c.data_atualizacao = datetime.now()
    db.session.commit()
    return jsonify({'success': True, 'notas': c.notas})

@app.route('/api/scrape', methods=['POST'])
def scrape():
    try:
        result = scrape_pci_concursos(db, Concurso)
        return jsonify({
            'success':     True,
            'novos':       result['novos'],
            'atualizados': result['atualizados'],
            'total':       result['total'],
            'timestamp':   datetime.now().isoformat(),
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats')
def get_stats():
    total = db.session.query(func.count(Concurso.id)).scalar()
    por_status = {s: db.session.query(func.count(Concurso.id)).filter_by(status=s).scalar()
                  for s in STATUS_CHOICES}
    por_regiao = {label: db.session.query(func.count(Concurso.id)).filter_by(regiao=k).scalar()
                  for k, label in REGIONS.items()}
    return jsonify({'total': total, 'por_status': por_status, 'por_regiao': por_regiao})

@app.route('/api/ufs')
def get_ufs():
    rows = db.session.query(Concurso.uf).distinct().order_by(Concurso.uf).all()
    return jsonify([r[0] for r in rows if r[0]])

@app.route('/api/concursos/<int:cid>/detail')
def get_detail(cid):
    c = db.session.get(Concurso, cid)
    if not c or not c.link:
        return jsonify({'cargos_lista': [], 'editais': []})
    try:
        resp = _requests.get(c.link, headers=_HEADERS, timeout=10)
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.content, 'html.parser')
        body = soup.find('div', attrs={'itemprop': 'articleBody'})

        # Extract cargo list from <ul><li> elements
        cargos_lista = []
        if body:
            for ul in body.find_all('ul'):
                items = [li.get_text(strip=True) for li in ul.find_all('li') if li.get_text(strip=True)]
                if items:
                    cargos_lista.extend(items)
                    break  # use first <ul> (usually the cargo list)

        # Extract all PDF links from the full page
        editais = []
        seen = set()
        for a in soup.find_all('a', href=True):
            href = a['href']
            if '.pdf' in href.lower() and href not in seen:
                seen.add(href)
                nome = a.get_text(strip=True) or 'Edital'
                editais.append({'nome': nome, 'url': href})

        return jsonify({'cargos_lista': cargos_lista, 'editais': editais})
    except Exception as e:
        return jsonify({'cargos_lista': [], 'editais': [], 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
