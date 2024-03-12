from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, LargeBinary, Boolean
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(500), nullable=True, unique=True)
    profilePicture = Column(LargeBinary, nullable=True)
    superUser = Column(Boolean, nullable=True, default=False)

    def __init__(self, nombre, password, email=None, profilePicture=None, superUser=False):
        self.nombre = nombre
        self.password = password
        self.email = email
        self.profilePicture = profilePicture
        self.superUser = superUser

    def __str__(self):
        return f'Usuario: {self.nombre}, Email: {self.email}'

class Pelicula(db.Model):
    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    genero = Column(String(45), nullable=True)
    duracion = Column(Integer, nullable=True)
    inventario = Column(Integer, nullable=False, default=1)

    def __init__(self, nombre, genero=None, duracion=None, inventario=1):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f'Película: {self.nombre}, Género: {self.genero}'

class Rentar(db.Model):
    __tablename__ = 'rentar'
    idRentar = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idUsuario = db.Column(db.Integer, db.ForeignKey('usuarios.idUsuario'), nullable=False)
    idPelicula = db.Column(db.Integer, db.ForeignKey('peliculas.idPelicula'), nullable=False)
    fecha_renta = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    dias_de_renta = db.Column(db.Integer, nullable=True, default=5)
    estatus = db.Column(db.Boolean, nullable=True, default=False)
    
    usuario = relationship('Usuario')
    pelicula = relationship('Pelicula')

    def __init__(self, idUsuario, idPelicula, fecha_renta, dias_de_renta=5, estatus=False):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

    def __str__(self):
        return f'Renta de {self.pelicula.nombre} a {self.usuario.nombre}, Fecha: {self.fecha_renta}'