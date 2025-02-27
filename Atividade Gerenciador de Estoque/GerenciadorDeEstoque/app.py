from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Autor, Livro, LivroAutor, Estoque

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    print("Banco de dados criado com sucesso!")

@app.route('/controle_saida')
def controle_saida():
    livros = Livro.query.all()
    return render_template('controle_saida.html', livros=livros)

@app.route('/controle_entrada')
def controle_entrada():
    livros = Livro.query.all()
    return render_template('controle_entrada.html', livros=livros)

@app.route('/cadastro_autor')
def cadastro_autor():
    return render_template('cadastro_autor.html')

@app.route('/cadastro_livro')
def cadastro_livro():
    return render_template('cadastro_livro.html')

@app.route('/controle_estoque')
def controle_estoque():
    livros = Livro.query.all()
    return render_template('controle_estoque.html', livros=livros)

@app.route('/excluir_livro/<int:livro_id>', methods=['POST'])
def excluir_livro(livro_id):
    livro = Livro.query.get(livro_id)
    if livro:
        db.session.delete(livro)
        db.session.commit()
        return jsonify({"mensagem": "Livro excluído com sucesso!"})
    return jsonify({"erro": "Livro não encontrado!"}), 404

@app.route('/cadastrar_autor', methods=['POST'])
def cadastrar_autor():
    nome = request.form.get('nome')
    nacionalidade = request.form.get('nacionalidade')
    biografia = request.form.get('biografia')

    if nome and nacionalidade and biografia:
        novo_autor = Autor(aut_nome=nome, aut_nacionalidade=nacionalidade, aut_biografia=biografia)
        try:
            db.session.add(novo_autor)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao inserir no banco: {e}")
        finally:
            db.session.close()

    return redirect(url_for('cadastro_autor'))

@app.route('/listar_autores')
def listar_autores():
    autores = Autor.query.all()
    autores_json = [{"id": autor.aut_id, "nome": autor.aut_nome} for autor in autores]
    return jsonify(autores_json)

@app.route('/cadastrar_livro', methods=['POST'])
def cadastrar_livro():
    data = request.json

    titulo = data.get('titulo')
    isbn = data.get('isbn')
    edicao = data.get('edicao')
    editora = data.get('editora')
    ano_publicacao = data.get('ano_publicacao')
    preco_capa = data.get('preco_capa')
    categoria = data.get('categoria')
    autor_id = data.get('autor_id')

    if not titulo or not autor_id:
        return jsonify({"mensagem": "Dados inválidos!"}), 400

    novo_livro = Livro(
        liv_titulo=titulo,
        liv_isbn=isbn,
        liv_edicao=edicao,
        liv_editora=editora,
        liv_ano_publicacao=ano_publicacao,
        liv_preco_capa=preco_capa,
        liv_categoria=categoria
    )

    db.session.add(novo_livro)
    db.session.commit()

    livro_autor = LivroAutor(lia_liv_id=novo_livro.liv_id, lia_aut_id=autor_id)
    db.session.add(livro_autor)
    db.session.commit()

    novo_estoque = Estoque(tbl_livro_liv_id=novo_livro.liv_id, est_quantidade=1)
    db.session.add(novo_estoque)
    db.session.commit()

    return jsonify({"mensagem": "Livro cadastrado com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)