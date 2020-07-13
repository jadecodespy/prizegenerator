import unittest, pytest
from flask import url_for
from flask_testing import TestCase
from os import getenv
from unittest.mock import patch
from app import app, db, Prizetable
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app


    


class TestGenerator(TestBase):
    def test_prizegiver(self):
        with requests_mock.mock() as p:
            p.get('http://service2:5001/numgen', text="3454")
            p.get('http://service3:5002/lettergen', text='D')
            p.post('http://service4:5003/codegenerator', text="Nothing")
            response = self.client.get('/prizegiver')
            self.assertIn(b'Nothing', response.data)
