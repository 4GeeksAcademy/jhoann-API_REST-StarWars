"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for,json
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Usuario,Planeta,Planeta_fav,Vehicle,Vehicle_fav,Personaje,Personaje_fav
from flask_jwt import create_access_token, get_jwt_identity, jwt_required, JWTManager

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

#  FINAL ENDPOINT USUARIOS GENERALES-USUARIO




#  INICIO ENDPOINT USUARIOS INDIVIDUALES


@app.route('/usuario/<int:id>', methods=['GET'])
def get_usuario_individual(id):
    results_ind = Usuario.query.filter_by(id=id).first()

    response_body = {
    "msg": "Hello, this is your GET /user response ",
    "result": results_ind.serialize()
    }


    return jsonify(response_body), 200

#  FINAL ENDPOINT USUARIOS INDIVIDUALES



#  INICIO ENDPOINT USUARIOS GENERALES-PLANETA


@app.route('/planets', methods=['GET'])
def get_planets():
    results_planet = Planeta.query.all()
    users_list = list(map(lambda item: item.serialize(),results_planet))

    response_body = {
        "msg": "Hello, this is your GET /planeta response ",
        "results": users_list
    }

    return jsonify(response_body), 200

#  FINAL ENDPOINT USUARIOS GENERALES-PLANETA



#  INICIO ENDPOINT PLANETAS-INDIVIDUALES


@app.route('/planets/<int:id>', methods=['GET'])
def get_planeta_individual(id):
    results_planeta = Planeta.query.filter_by(id=id).first()

    response_body = {
    "msg": "Hello, this is your GET /planeta by id response ",
    "result": results_planeta.serialize()
    }

    return jsonify(response_body), 200

#  FINAL ENDPOINT PLANETAS-INDIVIDUALES


#  INICIO ENDPOINT PERSONAJES  Listar todos los usuarios del blog

@app.route('/personajes', methods=['GET'])
def get_personajes():
    resp_users_personajes = Personaje.query.all()
    personajes_list = list(map(lambda item: item.serialize(),resp_users_personajes))

    response_body = {
        "msg": "Hello, this is your GET /personajes response ",
        "result": personajes_list
    }

    return jsonify(response_body), 200

#  FINAL ENDPOINT PERSONAJE   Listar todos los usuarios del blog

#  INICIO ENDPOINT PERSONAJE FAVORITO  Listar todos los usuarios del blog

@app.route('/personajes/<int:id>', methods=['GET'])
def get_personaje_favorito(id):
    results_personajes_individuales = Personaje.query.filter_by(id=id).first()

    response_body = {
        "msg": "Hello, this is your GET /personajes favoritos response ",
        "result": results_personajes_individuales.serialize()
    }

    return jsonify(response_body), 200


#  INICIO ENDPOINT Añade un nuevo planet favorito al usuario actual con el planet id = planet_id.  Listar todos los usuarios del blog

@app.route('/favorite/planet/<int:id>', methods=['POST'])
# Acceso protegido
def born_planet_fav(id):

    user_new_fav_planet = Usuario.query.filter_by(id=id).first()

    body = json.loads(request.data)

    if body is None:
        raise APIException("Debe especificar el cuerpo de la solicitud como un objeto json", status_code=400)
    if 'name' not in body:
        raise APIException('Te falta seleccionar un nombre del planeta a crear', status_code=400)
    if 'terrain' not in body:
        raise APIException('Te falta seleccionar las caracteristicas del terreno', status_code=400)
    if 'population' not in body:
        raise APIException('Te falta indicar la cantidad de personas en el planeta', status_code=400)
    
    print(body)
    fav_planeta_add = Planeta_fav( name=body["name"], terrain=body["terrain"],population=body["population"])
    db.session.add(fav_planeta_add)
    db.session.commit()

    response_body = {
        "msg": "El planeta ha sido creado",
    }

    return jsonify(response_body), 200

#  FINAL ENDPOINT Añade un nuevo planet favorito al usuario actual con el planet id = planet_id.  Listar todos los usuarios del blog




#INICIO




#Inicio ENDPOINT LOGIN

@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = Usuario.query.filter_by(email=email).first()
    # print(user.email)

    if user is None:
        return jsonify({"msg": "User does not exists"}), 404 

    #        None.email
    if email != user.email or password != user.password:
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)





# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
