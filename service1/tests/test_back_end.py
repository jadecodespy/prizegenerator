import unittest
from flask import url_for
from flask_testing import TestCase
from os import getenv
from unittest.mock import patch


class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    


class TestViews(TestBase):
     def test_prizegiver_view(self):
         response = self.client.get(url_for('home'))
         self.assertEqual(response.status_code, 200)
