from flask import Flask, jsonify, request

from models import Item, db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)


with app.app_context():
    db.create_all()


@app.route("/items", methods=["GET"])
def list_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items]), 200


@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json(silent=True) or {}
    nome = data.get("nome")
    descricao = data.get("descricao", "")

    if not nome or not str(nome).strip():
        return jsonify({"error": "O campo 'nome' é obrigatório."}), 400

    item = Item(nome=nome.strip(), descricao=descricao)
    db.session.add(item)
    db.session.commit()

    return jsonify(item.to_dict()), 201


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = db.session.get(Item, item_id)

    if not item:
        return jsonify({"error": "Item não encontrado."}), 404

    return jsonify(item.to_dict()), 200


@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = db.session.get(Item, item_id)

    if not item:
        return jsonify({"error": "Item não encontrado."}), 404

    data = request.get_json(silent=True) or {}
    nome = data.get("nome", item.nome)
    descricao = data.get("descricao", item.descricao)

    if not nome or not str(nome).strip():
        return jsonify({"error": "O campo 'nome' é obrigatório."}), 400

    item.nome = nome.strip()
    item.descricao = descricao
    db.session.commit()

    return jsonify(item.to_dict()), 200


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = db.session.get(Item, item_id)

    if not item:
        return jsonify({"error": "Item não encontrado."}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({"message": "Item removido com sucesso."}), 200


if __name__ == "__main__":
    app.run(debug=True)
