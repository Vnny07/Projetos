from flask_sqlalchemy import SQLAlchemy

# Instanciando o objeto do banco de dados
db = SQLAlchemy()


# Tabela de usuários
class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # Relacionamento com a tabela de tarefas
    tarefas = db.relationship('Tarefa', backref='usuario', lazy=True)


# Tabela de tarefas
class Tarefa(db.Model):
    __tablename__ = 'tarefas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    setor = db.Column(db.String(100), nullable=False)
    prioridade = db.Column(db.Enum('baixa', 'média', 'alta', name='prioridade_enum'), nullable=False)
    data_cadastro = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.Enum('a fazer', 'fazendo', 'pronto', name='status_enum'), default='a fazer')


# Função para criar o banco
def create_db(app):
    with app.app_context():
        db.create_all()