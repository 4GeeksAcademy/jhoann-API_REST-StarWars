from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    name = db.Column(db.String(250),unique=False, nullable=False)
    password = db.Column(db.String(250),unique=False, nullable=False)

    favorite_users = db.relationship('Favoritos', backref='usuario', lazy=True)
    planet_user_fav = db.relationship('Planet_fav', backref = 'usuario', lazy=True)
    fav_user = db.relationship('Users_fav',backref = 'usuario', lazy=True)
    fav_character = db.relationship('Personaje_fav', backref = 'usuario', lazy=True)


    def __repr__(self):
        return '<Usuario %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
            # do not serialize the password, its a security breach
        }
    

    
class Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False )
    eye_color = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    person_favorite = db.relationship('Favoritos', backref='personaje', lazy=True)
    fav_person = db.relationship('Personaje_fav', backref = 'personaje', lazy=True)


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
    planet_fav = db.relationship('Favoritos', backref ='planeta', lazy=True)
    fav_planet = db.relationship('Planet_fav', backref = 'planeta', lazy=True)


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
    vehicle_fav = db.relationship('Favoritos',backref='vehicle', lazy=True)
    

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
    
class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    personaje_id = db.Column(db.Integer,db.ForeignKey('personaje.id'))
    planeta_id = db.Column(db.Integer, db.ForeignKey('planeta.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))


    def __repr__(self):
        return f"{self.usuario.id}, {self.personaje.id}, {self.planeta.id}, {self.vehicle.id}"

    def serialize(self):
        return {
            "id": self.id,
            "usuario": self.usuario_id,
            "personaje": self.personaje_id,
            "planeta": self.planeta_id,
            "vehicle": self.vehicle_id

            # do not serialize the password, its a security breach
        }
    

class Planet_fav(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planeta_id = db.Column(db.Integer,db.ForeignKey('planeta.id'))
    usuario_planeta = db.Column(db.Integer,db.ForeignKey('usuario.id'))


    def __repr__(self):
        return '<Planeta_fav %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "planeta": self.planeta_id           
        }
    

class Users_fav(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    def __repr__(self):
        return f"{self.usuario.id}"

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id           
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
            "usuario_id": self.usuario_id           
        }



 