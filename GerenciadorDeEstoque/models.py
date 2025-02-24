from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    edicao = db.Column(db.String(10))
    editora = db.Column(db.String(100))
    ano_publicacao = db.Column(db.Integer)
    preco_capa = db.Column(db.Float)
    categoria = db.Column(db.String(50))

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    nacionalidade = db.Column(db.String(50))
    biografia = db.Column(db.Text)

livro_autor = db.Table('livro_autor',
    db.Column('livro_id', db.Integer, db.ForeignKey('livro.id'), primary_key=True),
    db.Column('autor_id', db.Integer, db.ForeignKey('autor.id'), primary_key=True)
)

class Estoque(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    livro_id = db.Column(db.Integer, db.ForeignKey('livro.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    data_entrada = db.Column(db.Date)
    data_saida = db.Column(db.Date)

    livro = db.relationship('Livro', backref=db.backref('estoque', lazy=True))