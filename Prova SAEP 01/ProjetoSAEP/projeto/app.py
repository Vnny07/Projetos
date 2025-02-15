from flask import Flask, render_template, request, redirect, url_for
from models import db, tbl_usuario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def home():
    return redirect(url_for('cadastro_usuario'))

@app.route("/cadastro_usuario", methods=["GET", "POST"])
def cadastro_usuario():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]

        novo_usuario = tbl_usuario(usu_nome=nome, usu_email=email)
        db.session.add(novo_usuario)
        db.session.commit()

        return "Usuário cadastrado com sucesso!"

    return render_template("cadastro_usuario.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)