import sqlite3
from .connection import ConectionDB


class Tareas:

    def __init__(self, beneficio_tarea, plazo_tarea):
        self.id_tarea = None
        self.beneficio_tarea = beneficio_tarea
        self.plazo_tarea = plazo_tarea

    def __str__(self):
        return f'Tarea[{self.beneficio_tarea},{self.plazo_tarea}]'


def crear_tabla_tareas() -> None:
    conexion = ConectionDB()
    puntero = conexion.cursor_tareas()

    sql = '''
    CREATE TABLE tareas(
        ID_TAREA INTEGER,
        BENEFICIO_TAREA INTEGER,
        PLAZO_TAREA INTEGER,

        PRIMARY KEY(ID_TAREA AUTOINCREMENT) 
    )
    '''
    try:
        puntero.execute(sql)
        conexion.close()
    except sqlite3.OperationalError:
        pass


def borrar_tabla_tareas() -> None:
    conexion = ConectionDB()
    puntero = conexion.cursor_tareas()
    sql = "DROP TABLE tareas"

    try:
        puntero.execute(sql)
        conexion.close()
    except sqlite3.OperationalError:
        pass


def ingresar_tarea(objeto: Tareas) -> None:
    conexion = ConectionDB()
    puntero = conexion.cursor_tareas()

    sql = "INSERT INTO tareas(BENEFICIO_TAREA, PLAZO_TAREA) VALUES(?,?)"
    data = (objeto.beneficio_tarea, objeto.plazo_tarea)
    puntero.execute(sql, data)
    conexion.close()


def editar_tarea(objeto: Tareas, id_tarea: int) -> None:
    conexion = ConectionDB()
    puntero = conexion.cursor_tareas()
    sql = "UPDATE tareas SET BENEFICIO_TAREA = ?, PLAZO_TAREA = ? WHERE ID_TAREA = ?"
    data = (objeto.beneficio_tarea, objeto.plazo_tarea, id_tarea)

    puntero.execute(sql, data)
    conexion.close()


def eliminar_tarea(id_tarea: int) -> None:
    conexion = ConectionDB()
    puntero = conexion.cursor_tareas()
    sql = "DELETE FROM tareas WHERE ID_TAREA = ?"
    data = (id_tarea,)

    puntero.execute(sql, data)
    conexion.close()

def listar_en_tabla()->list:
    conexion = ConectionDB()
    puntero = conexion.cursor_tareas()
    lista_tareas = []
    sql = 'SELECT * FROM tareas'
    try:
        puntero.execute(sql)
        lista_tareas = puntero.fetchall()
        conexion.close()
    except sqlite3.OperationalError:
        pass
    
    return lista_tareas
