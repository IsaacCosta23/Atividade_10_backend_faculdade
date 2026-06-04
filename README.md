# Flask CRUD API

API simples em Flask para criar, listar, atualizar e deletar itens usando SQLite e SQLAlchemy.

## Como rodar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute a aplicação:
   ```bash
   python app.py
   ```

A API ficará disponível em:
```text
http://127.0.0.1:5000
```

## Rotas

### Criar item
POST /items

Exemplo com curl:
```bash
curl -X POST http://127.0.0.1:5000/items \
  -H "Content-Type: application/json" \
  -d '{"nome":"Caneta","descricao":"Caneta azul"}'
```

### Listar itens
GET /items

```bash
curl http://127.0.0.1:5000/items
```

### Buscar item por ID
GET /items/1

```bash
curl http://127.0.0.1:5000/items/1
```

### Atualizar item
PUT /items/1

```bash
curl -X PUT http://127.0.0.1:5000/items/1 \
  -H "Content-Type: application/json" \
  -d '{"nome":"Caneta Atualizada","descricao":"Caneta azul nova"}'
```

### Deletar item
DELETE /items/1

```bash
curl -X DELETE http://127.0.0.1:5000/items/1
```
