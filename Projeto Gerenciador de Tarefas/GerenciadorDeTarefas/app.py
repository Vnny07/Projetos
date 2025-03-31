from flask import Flask, render_template, request, redirect, url_for
from models import db, Usuario, Tarefa, create_db

app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # Caminho do arquivo db.sqlite3
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa o rastreamento de modificações

# Inicializa o banco de dados
db.init_app(app)

# Cria o banco de dados (caso não exista)
create_db(app)


# Rota para a tela de cadastro de usuário
@app.route('/cadastro_usuario', methods=['GET', 'POST'])
def cadastro_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        # Criação do novo usuário
        novo_usuario = Usuario(nome=nome, email=email)

        try:
            db.session.add(novo_usuario)
            db.session.commit()
            mensagem = "Usuário cadastrado com sucesso!"
        except Exception as e:
            db.session.rollback()
            mensagem = f"Erro ao cadastrar usuário: {e}"

        return render_template('cadastro_usuario.html', mensagem=mensagem)

    return render_template('cadastro_usuario.html')


# Rota para a tela de cadastro de tarefa
@app.route('/cadastro_tarefa', methods=['GET', 'POST'])
def cadastro_tarefa():
    if request.method == 'POST':
        descricao = request.form['descricao']
        setor = request.form['setor']
        id_usuario = request.form['usuario']
        prioridade = request.form['prioridade']
        id_tarefa = request.form.get('id_tarefa')

        if id_tarefa:
            # Editando tarefa existente
            tarefa = Tarefa.query.get(id_tarefa)
            tarefa.descricao = descricao
            tarefa.setor = setor
            tarefa.prioridade = prioridade
            db.session.commit()
            mensagem = "Tarefa atualizada com sucesso!"
        else:
            # Criação de nova tarefa
            nova_tarefa = Tarefa(descricao=descricao, setor=setor, id_usuario=id_usuario, prioridade=prioridade)
            db.session.add(nova_tarefa)
            db.session.commit()
            mensagem = "Tarefa cadastrada com sucesso!"

        return render_template('cadastro_tarefa.html', mensagem=mensagem, usuarios=Usuario.query.all())

    # Se for GET, exibe a tarefa para edição
    id_tarefa = request.args.get('id_tarefa')
    tarefa = None
    if id_tarefa:
        tarefa = Tarefa.query.get(id_tarefa)

    return render_template('cadastro_tarefa.html', usuarios=Usuario.query.all(), tarefa=tarefa)


# Rota para a tela de gerenciamento de tarefas
@app.route('/')
def gerenciamento_tarefas():
    tarefas_a_fazer = Tarefa.query.filter_by(status='a fazer').all()
    tarefas_fazendo = Tarefa.query.filter_by(status='fazendo').all()
    tarefas_prontas = Tarefa.query.filter_by(status='pronto').all()
    return render_template('gerenciamento_tarefas.html', tarefas_a_fazer=tarefas_a_fazer,
                           tarefas_fazendo=tarefas_fazendo, tarefas_prontas=tarefas_prontas)


# Rota para atualizar o status da tarefa
@app.route('/atualizar_status/<int:id_tarefa>', methods=['POST'])
def atualizar_status(id_tarefa):
    tarefa = Tarefa.query.get(id_tarefa)
    novo_status = request.form['status']
    tarefa.status = novo_status
    db.session.commit()
    return redirect(url_for('gerenciamento_tarefas'))


# Rota para editar a tarefa
@app.route('/editar_tarefa/<int:id_tarefa>')
def editar_tarefa(id_tarefa):
    return redirect(url_for('cadastro_tarefa', id_tarefa=id_tarefa))


# Rota para excluir a tarefa
@app.route('/excluir_tarefa/<int:id_tarefa>', methods=['POST'])
def excluir_tarefa(id_tarefa):
    tarefa = Tarefa.query.get(id_tarefa)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for('gerenciamento_tarefas'))


if __name__ == '__main__':
    app.run(debug=True)