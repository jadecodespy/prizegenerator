from flask import render_template, request,Response, url_for, redirect
from application import app
import random
import requests


@app.route('/', methods = ['GET', 'POST'])
@app.route('/codegenerator', methods = ['GET', 'POST'])
def codegenerator():
    code = lettergen + numgen
    if code


