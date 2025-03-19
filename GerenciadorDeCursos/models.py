from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    carga_horaria = db.Column(db.Integer, nullable=False)
    instrutor = db.Column(db.String(100), nullable=False)

    inscricoes = db.relationship('Inscricao', backref='curso', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Curso {self.nome}>'

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=True)

    inscricoes = db.relationship('Inscricao', backref='aluno', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Aluno {self.nome}>'

class Inscricao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    data_inscricao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Inscricao Aluno {self.aluno_id} no Curso {self.curso_id}>'