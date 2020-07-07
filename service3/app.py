from flask import render_template, request, Response
import requests
import random

app=Flask(__name__)

@app.route('/lettergen', methods=['GET'])
def lettergen():
    letters=['A', 'B', 'C', 'D', 'E']
    return Response(letters[random.randint(0,4)], mimetype='text/plain')



if ___name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
