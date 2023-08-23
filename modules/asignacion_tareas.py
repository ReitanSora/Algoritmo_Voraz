import tkinter as tk
from tkinter import ttk
from functions import events as event
from functions.ordenamiento import Ordenamiento
from functions import funcion_asignacion_tareas as funcion
from static import style
from model.database_model import listar_en_tabla


class Asignacion(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background=style.BG)
        self.init_widgets()

    def ingresar_datos_tabla(self):
        self.lista_tareas = listar_en_tabla()
        orden = Ordenamiento()
        orden.ordenar_burbuja(self.lista_tareas)
        self.tabla.delete(*self.tabla.get_children())
        for tarea in self.lista_tareas:
            self.tabla.insert(parent='',index='end', text="", values= (tarea[0], tarea[1], tarea[2]))

    def ingresar_resultado_tabla(self, resultado:list):
        self.tabla.delete(*self.tabla.get_children())
        nueva_lista = []
        for i in resultado:
            #print(f'Elemento: {self.lista_tareas[i-1]}')
            nueva_lista.append(self.lista_tareas[i-1])
        #print(nueva_lista)
        for tarea in nueva_lista:
            self.tabla.insert(parent='',index='end', text="", values= (tarea[0], tarea[1], tarea[2]))

    def calcular(self):
        lista = listar_en_tabla()
        try:
            grupo = int(self.valor_grupo_tareas.get())
            self.texto_alerta_grupo_tareas.set('')
            if grupo > 2:
                resultado, beneficio = funcion.planificar(lista, grupo)
                self.valor_beneficio_obtenido.set(beneficio)
                self.ingresar_resultado_tabla(resultado)
            else:
                self.texto_alerta_grupo_tareas.set('Entero mayor a 2')
        except ValueError:
            self.texto_alerta_grupo_tareas.set('Ingrese un número entero')

    def init_widgets(self):

        # label para el titulo
        tk.Label(self,
                 text="Problema de asignación de tareas",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.X, pady=30)

        # frame donde se colocaran label y entry para datos que ingresa el usuario
        input_frame = tk.Frame(self, background=style.BG)
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(2, weight=1)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH)

        # label grupo de tareas
        tk.Label(input_frame,
                 text='Hasta el elemento',
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0, pady=(20, 0), padx=(0, 5), sticky=tk.E)

        # entry para el valor de grupo de tareas
        borde_entry_1 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_1.grid(row=0, column=1, pady=(30, 0), padx=0, sticky=tk.W)

        self.valor_grupo_tareas = tk.StringVar()
        entry_valor_grupo_tareas = tk.Entry(borde_entry_1,
                                            textvariable=self.valor_grupo_tareas,
                                            **style.STYLE_ENTRY,
                                            width=6,
                                            )
        entry_valor_grupo_tareas.pack(side=tk.TOP, fill=tk.X, expand=True)

        canvas_linea_1 = tk.Canvas(
            borde_entry_1, **style.STYLE_CANVAS, width=250)
        canvas_linea_1.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_1.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        self.texto_alerta_grupo_tareas = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_grupo_tareas,
                 **style.STYLE_WARNING,
                 ).pack()

        # boton para calcular
        borde_entry_2 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_2.grid(row=0, column=2, pady=(20, 0))

        borde_1 = tk.LabelFrame(borde_entry_2, **style.STYLE_BUTTON_BORDER)
        borde_1.pack()

        boton_calcular = tk.Button(borde_1,
                                   text="Calcular",
                                   **style.STYLE_BUTTON,
                                   command=self.calcular,
                                   )
        boton_calcular.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_calcular.bind('<Enter>', event.on_enter)
        boton_calcular.bind('<Leave>', event.on_leave)

        # frame donde se mostrara informacion acerca del grupo de tareas que fueron seleccionadas
        output_frame = tk.Frame(self, background=style.BG)
        output_frame.columnconfigure(0, weight=1)
        output_frame.columnconfigure(1, weight=1)
        output_frame.columnconfigure(2, weight=1)
        output_frame.pack(side=tk.TOP, fill=tk.BOTH)

        # tabla para representar las tareas seleccionadas del grupo de tareas
        self.tabla = ttk.Treeview(self,
                                  columns=("1", "2", "3"),
                                  selectmode="extended",
                                  )
        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH,
                        expand=True, padx=(20, 0), pady=20)
        self.ingresar_datos_tabla()

        # creación de una scrollbar
        self.scroll_table = tk.Scrollbar(self,
                                         border=0,
                                         orient="vertical",
                                         command=self.tabla.yview,
                                         )
        self.scroll_table.pack(side=tk.RIGHT, fill=tk.Y, pady=20, padx=0)
        self.tabla.config(yscrollcommand=self.scroll_table.set)

        # configuración de título, tamaño, centrado de cada columna
        self.tabla.column("#0", minwidth=0, width=0)
        self.tabla.heading("#1", text="Número de Tarea")
        self.tabla.column("#1", minwidth=0, width=320, anchor="center")
        self.tabla.heading("#2", text="Beneficio")
        self.tabla.column("#2", minwidth=0, width=320, anchor="center")
        self.tabla.heading("#3", text="Plazo")
        self.tabla.column("#3", minwidth=0, width=320, anchor="center")

        

        # label para el beneficio obtenido
        tk.Label(output_frame,
                 text='Beneficio Obtenido',
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0, pady=(40, 0), padx=(0, 5), sticky=tk.E)

        # entry desactivado para mostrar el valor del beneficio obtenido
        borde_entry_3 = tk.LabelFrame(output_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_3.grid(row=0, column=1, pady=(30, 0), padx=0, sticky=tk.W)

        self.valor_beneficio_obtenido = tk.StringVar()
        entry_valor_beneficio_obtenido = tk.Entry(borde_entry_3,
                                            textvariable=self.valor_beneficio_obtenido,
                                            **style.STYLE_ENTRY_DES,
                                            width=6,
                                            )
        entry_valor_beneficio_obtenido.pack(side=tk.TOP, fill=tk.X, expand=True)

        canvas_linea_3 = tk.Canvas(
            borde_entry_3, **style.STYLE_CANVAS, width=250)
        canvas_linea_3.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_3.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        # boton para calcular
        borde_entry_4 = tk.LabelFrame(output_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_4.grid(row=0, column=2, pady=(20, 0))

        borde_2 = tk.LabelFrame(borde_entry_4, **style.STYLE_BUTTON_BORDER)
        borde_2.pack()

        boton_resetear = tk.Button(borde_2,
                                   text="Ver todos",
                                   **style.STYLE_BUTTON,
                                   command=self.ingresar_datos_tabla,
                                   )
        boton_resetear.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_resetear.bind('<Enter>', event.on_enter)
        boton_resetear.bind('<Leave>', event.on_leave)
