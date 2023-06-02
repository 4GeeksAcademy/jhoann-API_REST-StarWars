"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Usuario, Planeta
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


#  INICIO ENDPOINT USUARIOS GENERALES-USUARIO

@app.route('/usuario', methods=['GET'])
def get_usuario():
    results = Usuario.query.all()
    users_list = list(map(lambda item: item.serialize(),results))


    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "results": users_list
    }

    return jsonify(response_body), 200


#  INICIO ENDPOINT USUARIOS INDIVIDUALES


@app.route('/usuario/<int:id>', methods=['GET'])
def get_usuario_individual(id):
    results_ind = Usuario.query.filter_by(id=id).first()

    response_body = {
    "msg": "Hello, this is your GET /user response ",
    "result": results_ind.serialize()
    }


    return jsonify(response_body), 200


#  INICIO ENDPOINT USUARIOS GENERALES-PLANETA


@app.route('/planeta', methods=['GET'])
def get_planets():
    results_planet = Planeta.query.all()
    users_list = list(map(lambda item: item.serialize(),results_planet))

    response_body = {
        "msg": "Hello, this is your GET /planeta response ",
        "results": users_list
    }

    return jsonify(response_body), 200


#  INICIO ENDPOINT PLANETAS-INDIVIDUALES


@app.route('/planeta/<int:id>', methods=['GET'])
def get_planeta_individual(id):
    results_planeta = Planeta.query.filter_by(id=id).first()

    response_body = {
    "msg": "Hello, this is your GET /planeta response ",
    "result": results_planeta.serialize()
    }

    return jsonify(response_body), 200








# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
