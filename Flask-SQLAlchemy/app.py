from flask import Flask
from models.models import db, Usuario, Pelicula, Rentar
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from sqlalchemy import and_, or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

# Funciones necesarias para realizar el punto 1
# "Ver los registros de una tabla"
def consultar_usuarios():
    usuarios = Usuario.query.all()
    print("Usuarios:")
    for usuario in usuarios:
        print(f"ID: {usuario.idUsuario}, Nombre: {usuario.nombre}, Email: {usuario.email}")

def consultar_peliculas():
    peliculas = Pelicula.query.all()
    print("Películas:")
    for pelicula in peliculas:
        print(f"ID: {pelicula.idPelicula}, Nombre: {pelicula.nombre}, Género: {pelicula.genero}, Duración: {pelicula.duracion} minutos")

def consultar_rentas():
    rentas = Rentar.query.all()
    print("Rentas:")
    for renta in rentas:
        usuario = Usuario.query.get(renta.idUsuario)
        pelicula = Pelicula.query.get(renta.idPelicula)
        print(f"ID Renta: {renta.idRentar}, Usuario: {usuario.nombre}, Película: {pelicula.nombre}, Fecha Renta: {renta.fecha_renta}")

def mostrar_registros(tabla):
    if tabla == 'usuarios':
        consultar_usuarios()
    elif tabla == 'peliculas':
        consultar_peliculas()
    elif tabla == 'rentar':
        consultar_rentas()
    else:
        print("Tabla no reconocida.")

# Función necesaria para realizar el punto 2
# "Filtrar los registros de una tabla por ID"
def filtrar_registro_por_id(tabla, id_registro):
    tabla_clase_mapa = {
        'usuarios': Usuario,
        'peliculas': Pelicula,
        'rentar': Rentar
    }
    modelo = tabla_clase_mapa.get(tabla)
    session = Session(bind=db.engine)

    if modelo:
        resultado = session.get(modelo, id_registro)
        if resultado:
            if tabla == 'usuarios':
                resultado = session.get(Usuario, id_registro)
                if resultado:
                    print(f"Usuario: ID {resultado.idUsuario}, Nombre: {resultado.nombre}, Email: {resultado.email}")
                else:
                    print(f"No se encontró un Usuario con el ID {id_registro}.")

            elif tabla == 'peliculas':
                resultado = session.get(Pelicula, id_registro)
                if resultado:
                    print(
                        f"Película: ID {resultado.idPelicula}, Nombre: {resultado.nombre}, Género: {resultado.genero}")
                else:
                    print(f"No se encontró una Película con el ID {id_registro}.")

            elif tabla == 'rentar':
                resultado = session.get(Rentar, id_registro)
                if resultado:
                    usuario = session.get(Usuario, resultado.idUsuario)
                    pelicula = session.get(Pelicula, resultado.idPelicula)
                    print(
                        f"Renta: ID {resultado.idRentar}, Usuario: {usuario.nombre if usuario else 'Desconocido'}, Película: {pelicula.nombre if pelicula else 'Desconocida'}, Fecha: {resultado.fecha_renta}")
                else:
                    print(f"No se encontró una Renta con el ID {id_registro}.")
    session.close()

# Funcion necesaria para el punto 3
# Actualizar la columna nombre de un registro
# Para actualizar nombre en las tablas "usuario" y "pelicula"
def actualizar_nombre(tabla, id_registro, nuevo_nombre):
    with app.app_context():
        session = db.session
        if tabla == 'usuarios':
            registro = session.query(Usuario).filter_by(idUsuario=id_registro).first()
        elif tabla == 'peliculas':
            registro = session.query(Pelicula).filter_by(idPelicula=id_registro).first()
        else:
            print("Tabla no reconocida.")
            return

        if registro:
            registro.nombre = nuevo_nombre
            session.commit()
            print(f"Nombre actualizado con éxito a '{nuevo_nombre}' para el registro con ID {id_registro} en la tabla {tabla}.")
        else:
            print(f"No se encontró el registro con ID {id_registro} en la tabla {tabla}.")

# Para actualizar la fecha de la tabla rentar
def actualizar_fecha_renta(id_renta, nueva_fecha):
    with app.app_context():
        session = db.session
        renta = session.query(Rentar).filter_by(idRentar=id_renta).first()

        if renta:
            renta.fecha_renta = nueva_fecha
            session.commit()
            print(f"Fecha de renta actualizada con éxito a '{nueva_fecha}' para la renta con ID {id_renta}.")
        else:
            print(f"No se encontró la renta con ID {id_renta}.")

# Función necesaria para el punto 4
# Eliminar un registro por ID o todos los registros
def eliminar_registro(tabla, id_registro=None):
    with app.app_context():
        tabla_clase_mapa = {
            'usuarios': Usuario,
            'peliculas': Pelicula,
            'rentar': Rentar,
        }

        modelo = tabla_clase_mapa.get(tabla)
        if not modelo:
            print("Nombre de tabla no reconocido.")
            return

        session = Session(bind=db.engine)

        try:
            if id_registro is not None:
                registro = session.get(modelo, id_registro)
                if registro:
                    session.delete(registro)
                    session.commit()
                    print(f"Registro con ID {id_registro} eliminado de la tabla {tabla}.")
                else:
                    print(f"No se encontró un registro con el ID {id_registro} en la tabla {tabla}.")
            else:
                session.query(modelo).delete()
                session.commit()
                print(f"Todos los registros eliminados de la tabla {tabla}.")
        except Exception as e:
            print(f"Error al eliminar registros: {e}")
        finally:
            session.close()

def mostrar_menu():
    print("\nMenú")
    print("1. Ver los registros de una tabla.")
    print("2. Filtrar los registros de una tabla por id.")
    print("3. Actualizar la columna nombre de un registro.")
    print("4. Eliminar un registro por id o todos los registros.")
    print("5. Salir")
def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            tabla = input("¿Qué tabla deseas consultar? (usuarios/peliculas/rentar): ")
            if tabla in ['usuarios', 'peliculas', 'rentar']:
                with app.app_context():
                    mostrar_registros(tabla)
            else:
                print("Tabla no reconocida.")


        elif opcion == '2':
            tabla = input("Ingresa el nombre de la tabla (usuarios/peliculas/rentar): ")
            id_registro = input("Ingresa el ID del registro a buscar: ")
            try:
                id_registro = int(id_registro)  # Asegurándose de que el ID es un entero
                with app.app_context():
                    filtrar_registro_por_id(tabla, id_registro)
            except ValueError:
                print("Por favor, ingresa un número válido para el ID.")


        elif opcion == '3':
            tabla = input("¿En qué tabla deseas realizar una actualización (usuarios/peliculas/rentar)?: ")
            id_registro = input("Ingresa el ID del registro a actualizar: ")
            if tabla in ['usuarios', 'peliculas']:
                nuevo_nombre = input("Ingresa el nuevo nombre: ")
                actualizar_nombre(tabla, int(id_registro), nuevo_nombre)
            elif tabla == 'rentar':
                nueva_fecha_str = input("Ingresa la nueva fecha de renta (YYYY-MM-DD): ")
                nueva_fecha = datetime.strptime(nueva_fecha_str, "%Y-%m-%d")
                actualizar_fecha_renta(int(id_registro), nueva_fecha)
            else:
                print("Opción de tabla no reconocida.")

        elif opcion == '4':
            tabla = input(
                "Ingresa el nombre de la tabla de la que deseas eliminar registros (usuarios/peliculas/rentar): ")
            if tabla not in ['usuarios', 'peliculas', 'rentar']:
                print("Tabla no reconocida.")
                continue
            eleccion = input("¿Deseas eliminar un registro específico o todos los registros? (específico/todos): ")
            if eleccion == 'especifico':
                id_registro = input("Ingresa el ID del registro a eliminar: ")
                try:
                    id_registro = int(id_registro)
                    eliminar_registro(tabla, id_registro)
                except ValueError:
                    print("Por favor, ingresa un número válido para el ID.")
            elif eleccion == 'todos':
                confirmacion = input(
                    "¿Estás seguro de que deseas eliminar TODOS los registros? Esto no se puede deshacer. (si/no): ")
                if confirmacion.lower() == 'si':
                    eliminar_registro(tabla)
                else:
                    print("Operación cancelada.")
            else:
                print("Opción no válida.")

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 5.")


if __name__ == '__main__':
    main()




