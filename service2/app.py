from flask import Flask, render_template, Response, request
import requests
import random

app=Flask(__name__)


@app.route('/numgen', methods=['GET'])
def numgen():
    randstring = ""
    for x in range(0,4):
        randnum=random.randint(1,10)
        randstring+=str(randnum)
    return Response(randstring, mimetype='text/plain')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)










