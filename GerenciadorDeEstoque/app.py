from flask import Flask, render_template, request, redirect, url_for
from models import db, Autor, Livro

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
@app.route('/cadastro_autor', methods=['GET', 'POST'])
def cadastro_autor():
    if request.method == 'POST':
        nome = request.form['nome']
        nacionalidade = request.form['nacionalidade']
        biografia = request.form['biografia']

        novo_autor = Autor(nome=nome, nacionalidade=nacionalidade, biografia=biografia)
        db.session.add(novo_autor)
        db.session.commit()

        return redirect(url_for('cadastro_autor'))

    return render_template('cadastro_autor.html')

@app.route('/cadastro_livro', methods=['GET', 'POST'])
def cadastro_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        isbn = request.form['isbn']
        edicao = request.form['edicao']
        editora = request.form['editora']
        ano_publicacao = request.form['ano_publicacao']
        preco_capa = request.form['preco_capa']
        categoria = request.form['categoria']
        autor_id = request.form['autor']

        novo_livro = Livro(
            titulo=titulo,
            isbn=isbn,
            edicao=edicao,
            editora=editora,
            ano_publicacao=int(ano_publicacao),
            preco_capa=float(preco_capa),
            categoria=categoria,
            autor_id=int(autor_id)
        )

        db.session.add(novo_livro)
        db.session.commit()

        return redirect(url_for('cadastro_livro'))

    autores = Autor.query.all()
    return render_template('cadastro_livro.html', autores=autores)

@app.route('/controle_estoque')
def controle_estoque():
    return render_template('controle_estoque.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Banco de dados criado com sucesso!")
    app.run(debug=True)