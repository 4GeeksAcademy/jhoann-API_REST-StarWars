from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usuario(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    # favorite_users = db.relationship('Favorito', backref='usuario', lazy=True)

    def __repr__(self):
        return '<Usuario %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
            # do not serialize the password, its a security breach
        }
    


class Personaje(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    # person_favorite = db.relationship('Favorito', backref='personaje', lazy=True)

    def __repr__(self):
        return '<Personaje %r>' % self.id

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
    # planet_fav =db.relationship('Favorito', backref='planeta', lazy=True)

    def __repr__(self):
        return '<Planeta %r>' % self.id

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
    # vehicle_fav = db.relationship('Favorito',backref='vehicle', lazy=True)
    

    def __repr__(self):
        return '<Vehicle %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "crew": self.crew,
            "vehicle_class": self.vehicle_class

            # do not serialize the password, its a security breach
        }
    
    # class Favorito(db.Model):
    #     id = db.Column(db.Integer, primary_key=True)
    #     usuario_id = db.Column(db.Integer, ForeignKey('usuario.id'))
    #     personaje_id = db.Column(db.Integer,ForeignKey('personaje.id'))
    #     planeta_id = db.Column(db.Integer, ForeignKey('planeta.id'))
    #     vehicle_id = db.Column(db.Integer, ForeignKey('vehicle.id'))


    

    
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