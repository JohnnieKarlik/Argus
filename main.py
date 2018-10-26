from flask import Flask, request
from flask_restful import Resource, Api
from requests import put
import argparse


app = Flask(__name__)
api = Api(app)

local_port = None
remote_address = None
msg = {}


class Echo(Resource):
    def get(self):
        return msg.get('msg')

    def put(self):
        msg['msg'] = request.form

    def post(self):
        msg['msg'] = request.get_json(force=True)
        result = put(remote_address, msg['msg'])
        return ('', 204)
        
api.add_resource(Echo, '/')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--local_port", type=int, default=5000)
    parser.add_argument("--remote_address", default="localhost:5001")
    args = parser.parse_args()
    local_port = args.local_port
    remote_address = args.remote_address
    app.run(debug=False, port=local_port)
