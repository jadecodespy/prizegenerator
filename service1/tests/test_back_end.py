import unittest, pytest
from flask import url_for
from flask_testing import TestCase
from os import getenv
<<<<<<< HEAD
from app import Prizetable, db, app 
from unittest.mock import patch
=======
from unittest.mock import patch
from app import app, db, Prizetable
import requests_mock
>>>>>>> 66801518bc32681fa58de3398c19bca30be8be07

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app


    
<<<<<<< HEAD
    def tearDown(self):
        db.session.remove()
        db.drop_all()



class TestResponse(TestBase):

    def test_num(self):
        with patch('request.get') as g:
            g.return_value.text = "Car"

            response = self.client.get(url_for('prizegiver'))
            self.assertIn(b'Car', response.data)









class TestViews(TestBase):
    def test_prizegiver_view(self):
        response = self.client.get(url_for('prizegiver'))
        self.assertEqual(response.status_code, 200)
=======


class TestGenerator(TestBase):
    def test_prizegiver(self):
        with requests_mock.mock() as p:
            p.get('http://service2:5001/numgen', text="3454")
            p.get('http://service3:5002/lettergen', text='D')
            p.post('http://service4:5003/codegenerator', text="Nothing")
            response = self.client.get('/prizegiver')
            self.assertIn(b'Nothing', response.data)
>>>>>>> 66801518bc32681fa58de3398c19bca30be8be07
