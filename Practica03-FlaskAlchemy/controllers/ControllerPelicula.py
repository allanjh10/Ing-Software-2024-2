from flask import Blueprint, request, render_template, flash, redirect, url_for
from models.models import db, Pelicula

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

# Listar todas las películas
@pelicula_blueprint.route('/')
def listar_peliculas():
    peliculas = Pelicula.query.all()
    return render_template('listar_peliculas.html', peliculas=peliculas)

# Agregar una nueva película
@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        genero = request.form.get('genero')
        duracion = request.form.get('duracion', type=int)
        inventario = request.form.get('inventario', default=1, type=int)

        nueva_pelicula = Pelicula(nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)
        db.session.add(nueva_pelicula)
        try:
            db.session.commit()
            flash('Película agregada con éxito.', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error al agregar la película. Por favor, intente nuevamente.', 'error')

        return redirect(url_for('pelicula.listar_peliculas'))

    return render_template('agregar_pelicula.html')

# Editar una película existente
@pelicula_blueprint.route('/editar/<int:idPelicula>', methods=['GET', 'POST'])
def editar_pelicula(idPelicula):
    pelicula = Pelicula.query.get_or_404(idPelicula)
    if request.method == 'POST':
        pelicula.nombre = request.form.get('nombre')
        pelicula.genero = request.form.get('genero')
        pelicula.duracion = request.form.get('duracion', type=int)
        pelicula.inventario = request.form.get('inventario', default=1, type=int)
        
        try:
            db.session.commit()
            flash('Película actualizada con éxito.', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error al actualizar la película.', 'error')
        
        return redirect(url_for('pelicula.listar_peliculas'))

    return render_template('editar_pelicula.html', pelicula=pelicula)

# Eliminar una película
@pelicula_blueprint.route('/eliminar/<int:idPelicula>', methods=['POST'])
def eliminar_pelicula(idPelicula):
    pelicula = Pelicula.query.get_or_404(idPelicula)
    try:
        db.session.delete(pelicula)
        db.session.commit()
        flash('Película eliminada con éxito.', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error al eliminar la película.', 'error')

    return redirect(url_for('pelicula.listar_peliculas'))
