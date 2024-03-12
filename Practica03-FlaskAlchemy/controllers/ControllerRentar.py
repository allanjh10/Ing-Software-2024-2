from flask import Blueprint, request, render_template, flash, redirect, url_for
from models.models import db, Rentar
from datetime import datetime, timedelta

rentar_blueprint = Blueprint('rentar', __name__, url_prefix='/rentar')

# Listar todas las rentas
@rentar_blueprint.route('/')
def listar_rentas():
    rentas = Rentar.query.all()
    fecha_actual = datetime.now()
    # Agrega un atributo 'vencida' a cada renta para su uso en la plantilla
    for renta in rentas:
        renta.vencida = (renta.fecha_renta + timedelta(days=renta.dias_de_renta)) < fecha_actual
    return render_template('listar_rentas.html', rentas=rentas)

# Agregar una nueva renta
@rentar_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'POST':
        idUsuario = request.form.get('idUsuario', type=int)
        idPelicula = request.form.get('idPelicula', type=int)
        fecha_renta = datetime.now()  # Suponemos que la renta inicia hoy
        # Otras configuraciones predeterminadas podrían incluirse aquí
        
        nueva_renta = Rentar(idUsuario=idUsuario, idPelicula=idPelicula, fecha_renta=fecha_renta)
        db.session.add(nueva_renta)
        try:
            db.session.commit()
            flash('Renta agregada con éxito.', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error al agregar la renta. Por favor, intente nuevamente.', 'error')

        return redirect(url_for('rentar.listar_rentas'))

    return render_template('agregar_renta.html')

# Actualizar estado de entrega de la renta
@rentar_blueprint.route('/actualizar/<int:idRentar>', methods=['GET', 'POST'])
def actualizar_renta(idRentar):
    renta = Rentar.query.get_or_404(idRentar)
    if request.method == 'POST':
        renta.estatus = not renta.estatus  # Cambia el estado de entrega
        try:
            db.session.commit()
            flash('Estado de renta actualizado con éxito.', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error al actualizar el estado de la renta.', 'error')

        return redirect(url_for('rentar.listar_rentas'))

    return render_template('actualizar_renta.html', renta=renta)
