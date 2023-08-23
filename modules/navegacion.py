'''
Tema: Métodos Numéricos
Grupo 6
Integrantes:

•	Kevin Josue Amaguaña Rivadeneira
•	Priscila Veronica Chisag Pillajo
•	Andy Ricardo Galarza Morales
•	Stiven Anthony Pilca Sánchez

Carrera: Ingeniería en Sistemas de la información
Paralelo: SI4 - 002
'''

import tkinter as tk
import functions.events as event
from static import style


class Navegacion (tk.Frame):

    def __init__(self, parent):
        super().__init__(master=parent)
        self.controller = parent
        self.configure(background=style.COLOR_MAGENTA_CLARO)
        self.init_widgets()

    def colorear_boton(self):
        if self.ubicacion.get() == 1:
            self.boton_inicio.configure(background=style.COLOR_MAGENTA_NORMAL)
            self.boton_ingreso_datos.configure(
                background=style.COLOR_MAGENTA_CLARO)
            self.boton_asignacion_tareas.configure(
                background=style.COLOR_MAGENTA_CLARO)
            self.deshabilitar_eventos()
        elif self.ubicacion.get() == 2:
            self.boton_ingreso_datos.configure(
                background=style.COLOR_MAGENTA_NORMAL)
            self.boton_inicio.configure(background=style.COLOR_MAGENTA_CLARO)
            self.boton_asignacion_tareas.configure(
                background=style.COLOR_MAGENTA_CLARO)
            self.deshabilitar_eventos()
        elif self.ubicacion.get() == 3:
            self.boton_asignacion_tareas.configure(
                background=style.COLOR_MAGENTA_NORMAL)
            self.boton_inicio.configure(background=style.COLOR_MAGENTA_CLARO)
            self.boton_ingreso_datos.configure(
                background=style.COLOR_MAGENTA_CLARO)
            self.deshabilitar_eventos()

    def deshabilitar_eventos(self):
        if self.ubicacion.get() == 1:
            self.boton_inicio.bind('<Leave>', event.on_enter_nav)
            self.boton_ingreso_datos.bind('<Leave>', event.on_leave_nav)
            self.boton_asignacion_tareas.bind('<Leave>', event.on_leave_nav)
        elif self.ubicacion.get() == 2:
            self.boton_ingreso_datos.bind('<Leave>', event.on_enter_nav)
            self.boton_inicio.bind('<Leave>', event.on_leave_nav)
            self.boton_asignacion_tareas.bind('<Leave>', event.on_leave_nav)
        elif self.ubicacion.get() == 3:
            self.boton_asignacion_tareas.bind('<Leave>', event.on_enter_nav)
            self.boton_inicio.bind('<Leave>', event.on_leave_nav)
            self.boton_ingreso_datos.bind('<Leave>', event.on_leave_nav)

    def home(self):
        self.controller.move_to_home()
        self.ubicacion.set(value=1)
        self.colorear_boton()

    def ingreso(self):
        self.controller.move_to_ingreso()
        self.ubicacion.set(value=2)
        self.colorear_boton()

    def asignacion(self):
        self.controller.move_to_asignacion()
        self.ubicacion.set(value=3)
        self.colorear_boton()

    def init_widgets(self):

        self.ubicacion = tk.IntVar(value=1)
        self.boton_inicio = tk.Button(self,
                                      text="Inicio",
                                      **style.STYLE_BUTTON_NAV,
                                      command=self.home
                                      )
        self.boton_inicio.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.boton_inicio.config(background=style.COLOR_MAGENTA_NORMAL)
        self.boton_inicio.bind('<Enter>', event.on_enter_nav)
        # self.boton_inicio.bind('<Leave>', event.on_leave_nav)

        self.boton_ingreso_datos = tk.Button(self,
                                             text="Ingresar\nTareas",
                                             **style.STYLE_BUTTON_NAV,
                                             command=self.ingreso
                                             )
        self.boton_ingreso_datos.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.boton_ingreso_datos.bind('<Enter>', event.on_enter_nav)
        self.boton_ingreso_datos.bind('<Leave>', event.on_leave_nav)

        self.boton_asignacion_tareas = tk.Button(self,
                                                 text="Asignación\nTareas",
                                                 **style.STYLE_BUTTON_NAV,
                                                 command=self.asignacion
                                                 )
        self.boton_asignacion_tareas.pack(
            side=tk.TOP, fill=tk.BOTH, expand=False)

        self.boton_asignacion_tareas.bind('<Enter>', event.on_enter_nav)
        self.boton_asignacion_tareas.bind('<Leave>', event.on_leave_nav)
