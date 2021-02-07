#import modules
import os
import secrets
import flask
import waitress
from flask import request, jsonify

#set global variables
global limit
global defaultnbytes
global limSTR

#set default limit and nbyte if not specified in docker
try:
    limit = os.environ['limit']
    limit = int(limit)
except:
    limit = 256

try:
    defaultnbytes = os.environ['default_nbytes']
    defaultnbytes = int(defaultnbytes)
except:
    defaultnbytes = 11

limSTR = str(limit)

#start flask server
app = flask.Flask(__name__)

#BYTE route
@app.route('/api/v1/byte', methods=['GET'])
def api_byte():
    def runByte():
        try:
            nbytes = int(request.args['nbytes'])
        except:
            nbytes = defaultnbytes

        global out
        if nbytes > limit:
            out = "Limit Exceeded! nbytes must be less than "+limSTR+"!"
        else:
            out = secrets.token_bytes(nbytes)
            out = {
                'status': 200,
                'message': 'OK',
                'key': out
            }
            out = str(out)

    runByte()
    return jsonify(out)

#URLsafe route
@app.route('/api/v1/urlsafe', methods=['GET'])
def api_URLsafe():
    def runURL():
        try:
            nbytes = int(request.args['nbytes'])
        except:
            nbytes = defaultnbytes

        global out
        if nbytes > limit:
            out = "Limit Exceeded! nbytes must be less than "+limSTR+"!"
        else:
            out = secrets.token_urlsafe(nbytes)
            out = {
                'status': 200,
                'message': 'OK',
                'key': out
            }

    runURL()
    return jsonify(out)

#randINT route
@app.route('/api/v1/randint', methods=['GET'])
def api_INT():
    def runINT():
        try:
            first = int(request.args['first'])
            last = int(request.args['last'])
        except:
            first = None
            last = None


        global out
        if None in (first, last):
            out = "Interger missing! [first] and [last] are required and must be an integer!"
        else:
            secretsGenerator = secrets.SystemRandom()
            out = secretsGenerator.randint(first,last)
            out = {
                'status': 200,
                'message': 'OK',
                'key': out
            }

    runINT()
    return jsonify(out)

#HEX route
@app.route('/api/v1/hex', methods=['GET'])
def api_hex():
    def runHEX():
        try:
            nbytes = int(request.args['nbytes'])
        except:
            nbytes = defaultnbytes

        global out
        if nbytes > limit:
            out = "Limit Exceeded! nbytes must be less than "+limSTR+"!"
        else:
            out = secrets.token_hex(nbytes)
            out = {
                'status': 200,
                'message': 'OK',
                'key': out
            }

    runHEX()
    return jsonify(out)

#Start server from waitress
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5050)