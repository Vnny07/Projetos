from flask import Flask, render_template, request, redirect, url_for
from models import db, Curso

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cursos')
def cursos():
    cursos_registrados = Curso.query.all()
    return render_template('cursos.html', cursos=cursos_registrados)

@app.route('/alunos')
def alunos():
    return render_template('alunos.html')

@app.route('/inscricoes')
def inscricoes():
    return render_template('inscricoes.html')

@app.route('/cadastrar_curso', methods=['GET', 'POST'])
def cadastrar_curso():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        carga_horaria = request.form['carga_horaria']
        instrutor = request.form['instrutor']

        novo_curso = Curso(
            nome=nome,
            descricao=descricao,
            carga_horaria=int(carga_horaria),
            instrutor=instrutor
        )
        db.session.add(novo_curso)
        db.session.commit()

        return redirect(url_for('cursos'))

    return render_template('cadastrar_curso.html')

@app.route('/editar_curso/<int:id>', methods=['GET', 'POST'])
def editar_curso(id):
    curso = Curso.query.get_or_404(id)

    if request.method == 'POST':
        curso.nome = request.form['nome']
        curso.descricao = request.form['descricao']
        curso.carga_horaria = request.form['carga_horaria']
        curso.instrutor = request.form['instrutor']

        db.session.commit()
        return redirect(url_for('cursos'))

    return render_template('editar_curso.html', curso=curso)

@app.route('/cadastrar_aluno')
def cadastrar_aluno():
    return render_template('cadastrar_aluno.html')

@app.route('/inscrever_aluno')
def inscrever_aluno():
    return render_template('inscrever_aluno.html')

@app.route('/excluir_curso/<int:id>')
def excluir_curso(id):
    curso = Curso.query.get(id)
    if curso:
        db.session.delete(curso)
        db.session.commit()
    return redirect(url_for('cursos'))

if __name__ == '__main__':
    app.run(debug=True)