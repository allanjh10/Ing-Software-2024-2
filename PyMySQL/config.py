import pymysql
import pymysql.cursors
from datetime import datetime, timedelta

# Función para obtener conexión
def obtener_conexion():
    return pymysql.connect(host='localhost',
                           user='lab',
                           password='Developer123!',
                           database='lab_ing_software', 
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

# 1. Función para insertar registros
def insertar_registros():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Insertar un usuario
            cursor.execute("INSERT INTO usuarios (nombre, password, email) VALUES ('Arya Pérez', 'password123', 'arya@example.com')")
            id_usuario = cursor.lastrowid
            
            # Insertar una película
            cursor.execute("INSERT INTO peliculas (nombre, genero, duracion) VALUES ('The Lobster', 'Ciencia Ficción', 150)")
            id_pelicula = cursor.lastrowid
            
            # Insertar una renta, asumiendo que la fecha actual es la de la renta
            cursor.execute("INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, NOW(), 5, 1)", (id_usuario, id_pelicula))
        
        conexion.commit()
        print("Registros insertados correctamente.")
    except Exception as e:
        print(f"Error al insertar registros: {e}")
    finally:
        conexion.close()

# 2. Función para filtrar usuarios por apellido
def filtrar_usuarios_por_apellido(terminacion_apellido):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE nombre LIKE %s", ('%' + terminacion_apellido))
            resultados = cursor.fetchall()
            for usuario in resultados:
                print(usuario)
    except Exception as e:
        print(f"Error al filtrar usuarios: {e}")
    finally:
        conexion.close()

# 3. Función para cambiar el género de una película
def cambiar_genero_pelicula(nombre_pelicula, nuevo_genero):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE peliculas SET genero = %s WHERE nombre = %s", (nuevo_genero, nombre_pelicula))
            conexion.commit()
            print(f"Género actualizado para la película {nombre_pelicula}.")
    except Exception as e:
        print(f"Error al actualizar género de la película: {e}")
    finally:
        conexion.close()

# 4. Función para eliminar rentas antiguas
def eliminar_rentas_antiguas():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            fecha_limite = datetime.now() - timedelta(days=3)
            cursor.execute("DELETE FROM rentar WHERE fecha_renta <= %s", (fecha_limite,))
            conexion.commit()
            print("Rentas antiguas eliminadas correctamente.")
    except Exception as e:
        print(f"Error al eliminar rentas antiguas: {e}")
    finally:
        conexion.close()

if __name__ == "__main__":
    insertar_registros()
    filtrar_usuarios_por_apellido('Pérez')
    cambiar_genero_pelicula('The Lobster', 'Sci-Fi')
    eliminar_rentas_antiguas()
