import unittest

from app import app, db


class ItemCrudTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_crud_flow(self):
        create_response = self.app.post('/items', json={'nome': 'Caneta', 'descricao': 'Azul'})
        self.assertEqual(create_response.status_code, 201)
        created_item = create_response.get_json()
        self.assertEqual(created_item['nome'], 'Caneta')
        item_id = created_item['id']

        list_response = self.app.get('/items')
        self.assertEqual(list_response.status_code, 200)
        self.assertGreaterEqual(len(list_response.get_json()), 1)

        get_response = self.app.get(f'/items/{item_id}')
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_response.get_json()['id'], item_id)

        update_response = self.app.put(f'/items/{item_id}', json={'nome': 'Caneta Atualizada', 'descricao': 'Nova'})
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.get_json()['nome'], 'Caneta Atualizada')

        delete_response = self.app.delete(f'/items/{item_id}')
        self.assertEqual(delete_response.status_code, 200)
        self.assertIn('sucesso', delete_response.get_json()['message'])

        not_found_response = self.app.get(f'/items/{item_id}')
        self.assertEqual(not_found_response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
