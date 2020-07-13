from flask_testing import TestCase
from application import app
from flask import url_for


class TestBase(TestCase):
    def create_app(self):
        return app


class TestPrize(TestBase):
    def test_generate_car(self):
        response=self.client.post('/codegenerator', data='C10627')
        self.assertIn(b'Car', response.data)


    def test_generate_chocolate(self):
        response=self.client.post('/codegenerator', data='D4789')
        self.assertIn(b'Chocolate', response.data)
    
    def test_generate_nothing(self):
        response=self.client.post('/codegenerator', data='A9736')
        self.assertIn(b'Nothing', response.data)

