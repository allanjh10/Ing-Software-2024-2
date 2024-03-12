# controllers/ControllerUsuario.py

from flask import Blueprint, request, render_template, flash, redirect, url_for
from models.models import db, Usuario
from werkzeug.security import generate_password_hash

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('listar_usuarios.html', usuarios=usuarios)

@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        password = request.form.get('password')
        email = request.form.get('email')
        superUser = True if request.form.get('superUser') == 'on' else False
        #hashed_password = generate_password_hash(password)
        nuevo_usuario = Usuario(nombre=nombre, password=password, email=email, superUser=superUser)
        db.session.add(nuevo_usuario)
        try:
            db.session.commit()
            flash('Usuario agregado con éxito', 'success')
        except Exception as e:
            db.session.rollback()
            print(e)
            flash('Error al agregar el usuario. Por favor, intente nuevamente.', 'error')
        
        return redirect(url_for('usuario.listar_usuarios'))
    
    return render_template('agregar_usuario.html')

@usuario_blueprint.route('/editar/<int:idUsuario>', methods=['GET', 'POST'])
def editar_usuario(idUsuario):
    usuario = Usuario.query.get_or_404(idUsuario)
    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.email = request.form['email']
        # No actualizamos password por simplicidad y seguridad.
        # La foto de perfil no se actualiza.
        usuario.superUser = True if 'superUser' in request.form else False
        db.session.commit()
        flash('Usuario actualizado con éxito.')
        return redirect(url_for('usuario.listar_usuarios'))

    return render_template('editar_usuario.html', usuario=usuario)

@usuario_blueprint.route('/eliminar/<int:idUsuario>', methods=['GET', 'POST'])
def eliminar_usuario(idUsuario):
    usuario = Usuario.query.get_or_404(idUsuario)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado con éxito.')
    return redirect(url_for('usuario.listar_usuarios'))
