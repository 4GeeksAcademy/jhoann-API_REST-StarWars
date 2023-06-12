from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    name = db.Column(db.String(250),unique=False, nullable=False)
    password = db.Column(db.String(250),unique=False, nullable=False)
    
    planet_fav_user = db.relationship('Planeta_fav', backref = 'usuario', lazy=True)
    Vehicle_fav_user = db.relationship('Vehicle_fav', backref = 'usuario', lazy=True)
    Personaje_fav_user = db.relationship('Personaje_fav', backref = 'usuario', lazy=True)

    def __repr__(self):
        return '<Usuario %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
            # do not serialize the password, its a security breach
        }
    
class Planeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    planet_fav = db.relationship('Planeta_fav', backref = 'planeta', lazy=True)

    def __repr__(self):
        return '<Planeta %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain
        }


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.String(250), nullable=False)
    vehicle_class = db.Column(db.String(250), nullable=False)
    fav_vehicle = db.relationship('Vehicle_fav', backref = 'vehicle', lazy=True)

    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "crew": self.crew,
            "vehicle_class": self.vehicle_class

        }


class Personaje(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    fav_person = db.relationship('Personaje_fav', backref = 'personaje', lazy=True)
    
    def __repr__(self):
        return '<Personaje %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "hair_color":self.hair_color
        }

# INICIO TABLAS FAVORITOS

class Planeta_fav(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_fav_user= db.Column(db.Integer,db.ForeignKey('usuario.id'))
    planeta_fav_id = db.Column(db.Integer,db.ForeignKey('planeta.id'))

    def __repr__(self):
        return '<Planeta_fav %r>' % self.id


    def serialize(self):
        return {
            "id": self.id,
            "name": self.planeta_tab_principal_name,
            "id_planeta_fav": self.planet_fav_user,
            "planeta_fav_select": self.planeta_fav_id

        }


class Vehicle_fav(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))

    def __repr__(self):
        return   '<Vehicle_fav %r>' % self.id


    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "vehicle_select": self.vehicle_id
         }


class Personaje_fav(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    personaje_id = db.Column(db.Integer, db.ForeignKey('personaje.id'))

    def __repr__(self):
        return '<Personaje_fav %r>' % self.id


    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "fav_person": self.personaje_id
            }