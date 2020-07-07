from flask import Flask, render_template, Response, request
import requests
import random

app=Flask(__name__)


@app.route('numgen', methods=['GET'])
def numgen():
    randomlist=()
    for x in range(0,4):
        randnum=random.randint(1,10)
        randmomlist.append(n)
        return Response(randnum, mimetype='text/plain')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)














if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
