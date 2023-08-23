

import tkinter as tk
import os
from static import style
from modules.home import Home
from modules.navegacion import Navegacion
from modules.ingreso_datos import Ingreso
from modules.asignacion_tareas import Asignacion
from model.database_model import crear_tabla_tareas

class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        # metodo constructor de la clase Tk
        super().__init__(*args, **kwargs)
        crear_tabla_tareas()
        self.title("Métodos Numéricos")
        self.geometry("1000x700")
        self.resizable(False, False)
        self.start_pos = -0.2
        final_pos = 0
        self.pos_inicio = self.start_pos + 0.05
        self.pos_final = final_pos - 0.02
        self.width = abs(self.start_pos - final_pos)
        self.pos = self.start_pos
        self.estado_pos = True
        self.estado_color = False

        ruta_icono = os.path.abspath("./static/resources/icon.ico")
        self.iconbitmap(ruta_icono)

        barra_toggle = tk.LabelFrame(self, **style.STYLE_ENTRY_BORDER)
        barra_toggle.pack(side=tk.TOP, fill=tk.X)
        barra_toggle.configure(highlightthickness=2,
                               highlightbackground=style.COLOR_MAGENTA_CLARO)

        borde_toggle = tk.LabelFrame(barra_toggle, **style.STYLE_ENTRY_BORDER)
        borde_toggle.pack(side=tk.LEFT)

        self.canvas_linea_1 = tk.Canvas(
            borde_toggle, **style.STYLE_CANVAS_TOGGLE, width=30, cursor='hand2')
        self.canvas_linea_1.pack(
            side=tk.TOP, anchor=tk.CENTER, padx=20, pady=20, fill=tk.BOTH, expand=True)
        self.linea_1 = self.canvas_linea_1.create_line(
            0, 4, 30, 4, **style.STYLE_CANVAS_LINE)
        self.linea_2 = self.canvas_linea_1.create_line(
            0, 14, 30, 14, **style.STYLE_CANVAS_LINE)
        self.linea_3 = self.canvas_linea_1.create_line(
            0, 24, 30, 24, **style.STYLE_CANVAS_LINE)
        self.canvas_linea_1.bind('<ButtonRelease>', self.animacion)
        self.canvas_linea_1.bind('<ButtonPress>', self.toggle_color)

        # titulo principal para el programa
        tk.Label(barra_toggle,
                 text="Algoritmos",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.LEFT, fill=tk.BOTH, padx=30)

        # label de información - footer
        tk.Label(barra_toggle,
                 text="Proyecto Final\nGrupo-3",
                 font=("Corbel", 10, "normal"),
                 background=style.BG,
                 foreground="#FFF",
                 ).pack(side=tk.RIGHT, fill=tk.BOTH, padx=40)

        # contenedor donde se mostrarán todas las demás ventanas
        self.container = tk.Frame(self)
        self.container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.container.configure(background=style.BG, bd=0)

        # contenedor para los botones de navegacion
        self.frame = Navegacion(self)
        self.frame.place(relx=self.start_pos, rely=0.115,
                         relwidth=self.width, relheight=0.5)

        # creacion de filas y clumnas disponibles en el frame container,
        # 0 = 1 columna/fila ; weight = espacio que ocupa
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)

        # diccionario de clases
        self.frames = {}

        for F in (Home, Ingreso, Asignacion):
            frame = F(self.container, self)
            self.frames[F] = frame

            # configuracion de filas, columnas y rellenado del frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.show_frame(Home)

    # metodo para mostrar las diferentes ventanas
    def show_frame(self, container):
        frame = self.frames[container]

        # para poner una pantalla encima de la otra
        frame.focus()
        frame.tkraise()

    def animacion(self, e):
        if self.estado_pos:
            self.animacion_entrada()
        else:
            self.animacion_salida()

    def animacion_entrada(self):
        if self.pos < self.pos_final:
            self.pos += 0.008
            self.frame.place(relx=self.pos+0.05, rely=0.115,
                             relwidth=self.width, relheight=0.5)
            self.after(15, self.animacion_entrada)
        else:
            self.estado_pos = False

    def animacion_salida(self):
        if self.pos+0.05 > self.start_pos:
            self.pos -= 0.008
            self.frame.place(relx=self.pos+0.05, rely=0.115,
                             relwidth=self.width, relheight=0.5)
            self.after(15, self.animacion_salida)
        else:
            self.estado_pos = True

    def toggle_color(self, e):
        if (self.estado_color is False) and (self.estado_pos is True):
            self.canvas_linea_1.itemconfig(
                self.linea_1, fill=style.COLOR_BLANCO)
            self.canvas_linea_1.itemconfig(
                self.linea_2, fill=style.COLOR_BLANCO)
            self.canvas_linea_1.itemconfig(
                self.linea_3, fill=style.COLOR_BLANCO)
            self.canvas_linea_1.coords(self.linea_1, 0, 0, 30, 30)
            self.canvas_linea_1.coords(self.linea_2, 0, 0, 30, 30)
            self.canvas_linea_1.coords(self.linea_3, 0, 30, 30, 0)
            self.estado_color = True
        else:
            self.canvas_linea_1.itemconfig(
                self.linea_1, fill=style.COLOR_MAGENTA_CLARO)
            self.canvas_linea_1.itemconfig(
                self.linea_2, fill=style.COLOR_MAGENTA_CLARO)
            self.canvas_linea_1.itemconfig(
                self.linea_3, fill=style.COLOR_MAGENTA_CLARO)
            self.canvas_linea_1.coords(self.linea_1, 0, 4, 30, 4)
            self.canvas_linea_1.coords(self.linea_2, 0, 14, 30, 14)
            self.canvas_linea_1.coords(self.linea_3, 0, 24, 30, 24)
            self.estado_color = False

    def move_to_home(self):
        self.show_frame(Home)

    def move_to_ingreso(self):
        self.show_frame(Ingreso)

    def move_to_asignacion(self):
        self.show_frame(Asignacion)
