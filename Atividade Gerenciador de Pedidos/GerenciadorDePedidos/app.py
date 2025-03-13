from flask import Flask, render_template
from models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/clientes")
def clientes():
    return render_template("clientes.html")

@app.route("/pedidos")
def pedidos():
    return render_template("pedidos.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

@app.route("/novo_cliente")
def novo_cliente():
    return render_template("novo_cliente.html")

@app.route("/editar_cliente")
def editar_cliente():
    return render_template("editar_cliente.html")

@app.route("/editar_produto")
def editar_produto():
    return render_template("editar_produto.html")

@app.route("/novo_produto")
def novo_produto():
    return render_template("novo_produto.html")

@app.route("/editar_pedido")
def editar_pedido():
    return render_template("editar_pedido.html")

@app.route("/novo_pedido")
def novo_pedido():
    return render_template("novo_pedido.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    print("Banco de dados criado!")
    app.run(debug=True)