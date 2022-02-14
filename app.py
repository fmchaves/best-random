from src.server.instance import server
from src.controllers import *

@server.app.route('/')
def index():
    return "<h1>Welcome to Best Random API</h1>"

if __name__ == '__main__':
    server.run(True)
