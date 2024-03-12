from flask import Flask
from models.models import db, Usuario, Pelicula, Rentar
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from sqlalchemy import and_, or_
from controllers.ControllerUsuario import usuario_blueprint
from controllers.ControllerPelicula import pelicula_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)
app.register_blueprint(usuario_blueprint)
app.register_blueprint(pelicula_blueprint)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()