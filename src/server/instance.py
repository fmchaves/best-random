from flask import Flask
from flask_cors import CORS
from secrets import token_hex


class Server:

    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = token_hex()
        CORS(self.app)

    def run(self, debug=True):
        self.app.run(debug=debug)


server = Server()
