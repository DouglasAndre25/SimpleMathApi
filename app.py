from flask import Flask
from flask_restful import Api

from src.routes import Routes

app = Flask(__name__)
api = Api(app)

Routes(api)

if __name__ == '__main__':
    app.run(debug=True)