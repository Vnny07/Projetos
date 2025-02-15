from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class tbl_usuario(db.Model):
    usu_id = db.Column(db.Integer, primary_key=True)
    usu_nome = db.Column(db.String(100), nullable=False)
    usu_email = db.Column(db.String(100), unique=True, nullable=False)

class tbl_setor(db.Model):
    set_id = db.Column(db.Integer, primary_key=True)
    set_nome = db.Column(db.String(100), unique=True, nullable=False)

class tbl_tarefa(db.Model):
    tar_id = db.Column(db.Integer, primary_key=True)
    tar_descricao = db.Column(db.String(250), nullable=False)
    tar_prioridade = db.Column(db.String(20), nullable=False, default="Baixa")
    tar_status = db.Column(db.String(20), default="A fazer")
    tar_data_cadastro = db.Column(db.DateTime, default=db.func.current_timestamp())

    usu_id = db.Column(db.Integer, db.ForeignKey('tbl_usuario.usu_id'), nullable=False)
    set_id = db.Column(db.Integer, db.ForeignKey('tbl_setor.set_id'), nullable=False)

    usuario = db.relationship('tbl_usuario', backref=db.backref('tarefas', lazy=True))
    setor = db.relationship('tbl_setor', backref=db.backref('tarefas', lazy=True))