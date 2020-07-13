from flask_testing import TestCase
from app import app
from flask import url_for
import random

class TestBase(TestCase):
    def create_app(self):
        return app


class TestService2(TestBase):
    def test_num_gen(self):
        for i in range(10):
            response=self.client.get('/numgen')
            self.assertIs(type(response.data.decode('UTF-8')), str)
