from flask import Flask, render_template, url_for
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app= Flask(__name__)

db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')


class Prizetable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code= db.Column(db.String(30))
    prize= db.Column(db.String(30))



@app.route('/', methods=['GET'])
def prizegiver():
    num = requests.get('http://service2:5001/numgen')
    letter = requests.get('http://service3:5002/lettergen')
    code = letter.text + num.text
    prize = requests.post('http://service4:5003/codegenerator', data=code)
    
    new_prize=Prizetable(code=code, prize=prize.text)

    db.session.add(new_prize)
    db.session.commit()
    
    return render_template('home.html', code=code, prize=prize.text)

    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
