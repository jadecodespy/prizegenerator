from flask_testing import TestCase
from app import app
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        return app


class TestService3(TestBase):
    def test_letter_gen(self):
        response=self.client.get('/lettergen')
        self.assertIn(response.data.decode('UTF-8'), ['A','B','C','D','E'])


