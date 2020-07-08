from flask import render_template, request,Response, url_for, redirect
from application import app
import random
import requests


@app.route('/', methods = ['GET', 'POST'])
@app.route('/codegenerator', methods = ['GET', 'POST'])
def codegenerator():
    code = request.data.decode('utf-8')
    if code[0] == 'C' and code[1] == '1':
        prize ='Car'
    elif code[4] == '9':
        prize = 'Chocolate'
    else:
        prize = 'Nothing'

    return Response(prize, mimetype='text/plain')


