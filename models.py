from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Concurso(db.Model):
    __tablename__ = 'concursos'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False, index=True)
    orgao = db.Column(db.String(255), nullable=True)
    uf = db.Column(db.String(2), nullable=True, index=True)
    regiao = db.Column(db.String(50), nullable=False, index=True)
    link = db.Column(db.String(500), nullable=True, unique=True)
    cargos = db.Column(db.Text, nullable=True)
    escolaridade = db.Column(db.String(100), nullable=True)
    vagas = db.Column(db.String(100), nullable=True)
    prazo = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(50), default='Ainda não classificados', index=True)
    notas = db.Column(db.Text, default='')
    data_encontrado = db.Column(db.DateTime, default=datetime.now, index=True)
    data_atualizacao = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'<Concurso {self.titulo}>'

    @staticmethod
    def encontrar_por_link(link):
        if not link:
            return None
        return Concurso.query.filter_by(link=link).first()
