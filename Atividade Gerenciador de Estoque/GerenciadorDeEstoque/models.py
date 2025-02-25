from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Livro(db.Model):
    __tablename__ = 'tbl_livro'
    liv_id = db.Column(db.Integer, primary_key=True)
    liv_titulo = db.Column(db.String(150), nullable=False)
    liv_isbn = db.Column(db.String(20), unique=True)
    liv_edicao = db.Column(db.String(100))
    liv_editora = db.Column(db.String(100))
    liv_ano_publicacao = db.Column(db.String(4))
    liv_preco_capa = db.Column(db.Float)
    liv_categoria = db.Column(db.String(50))
    estoque = db.relationship('Estoque', backref='livro', lazy=True)
    autores = db.relationship('LivroAutor', backref='livro', lazy=True)

class Autor(db.Model):
    __tablename__ = 'tbl_autor'
    aut_id = db.Column(db.Integer, primary_key=True)
    aut_nome = db.Column(db.String(100), nullable=False)
    aut_nacionalidade = db.Column(db.String(50))
    aut_biografia = db.Column(db.String(100))
    livros = db.relationship('LivroAutor', backref='autor', lazy=True)

class LivroAutor(db.Model):
    __tablename__ = 'tbl_livro_autor'
    lia_liv_id = db.Column(db.Integer, db.ForeignKey('tbl_livro.liv_id'), primary_key=True)
    lia_aut_id = db.Column(db.Integer, db.ForeignKey('tbl_autor.aut_id'), primary_key=True)

class Estoque(db.Model):
    __tablename__ = 'tbl_estoque'
    est_id = db.Column(db.Integer, primary_key=True)
    est_quantidade = db.Column(db.Integer, nullable=False)
    est_data_entrada = db.Column(db.Date)
    est_data_saida = db.Column(db.Date, nullable=True)
    tbl_livro_liv_id = db.Column(db.Integer, db.ForeignKey('tbl_livro.liv_id'), nullable=False)