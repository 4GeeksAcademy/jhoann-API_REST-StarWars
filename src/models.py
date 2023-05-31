from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usuario(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Usuario %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
            # do not serialize the password, its a security breach
        }
    
class Personaje(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True , nullable=False )
    eye_color = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Personaje %r>' % self.name 

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color

            # do not serialize the password, its a security breach
        }

class Planeta(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planeta %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain

            # do not serialize the password, its a security breach
        }
    
    
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.String(250), nullable=False)
    vehicle_class = db.Column(db.String(250), nullable=False)
    

    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "crew": self.crew,
            "vehicle_class": self.vehicle_class

            # do not serialize the password, its a security breach
        }
    
class Favorito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    personaje_id = db.Column(db.Integer,db.ForeignKey('personaje.id'))
    planeta_id = db.Column(db.Integer, db.ForeignKey('planeta.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))

    usuario = db.relationship(Usuario)
    personaje = db.relationship(Personaje)
    planeta = db.relationship(Planeta)
    vehicle = db.relationship(Vehicle)


    def __repr__(self):
        return f" {self.usuario.id}, {self.personaje.name}, {self.planeta.name}, {self.vehicle.name}"

    def serialize(self):
        return {
            "id": self.id,
            "usuario": self.usuario_id,
            "personaje": self.personaje_id,
            "planeta": self.planeta_id,
            "vehicle": self.vehicle_id

            # do not serialize the password, its a security breach
        }




    

    
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }