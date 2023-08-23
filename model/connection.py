import sqlite3
import os


class ConectionDB:

    def __init__(self):
        ruta = os.path.abspath("./database/tareas.db")
        self.base_datos_tareas = ruta
        self.conexion_tareas = sqlite3.connect(self.base_datos_tareas)
        self.cursor_tareas = self.conexion_tareas.cursor

    def close(self):
        self.conexion_tareas.commit()
        self.conexion_tareas.close()
