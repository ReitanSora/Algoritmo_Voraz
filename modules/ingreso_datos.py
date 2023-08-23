import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functions import events as event
from static import style
from model.database_model import Tareas
from model.database_model import *

class Ingreso(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background=style.BG)
        self.id_tarea = None
        #self.resetear_tabla()
        self.init_widgets()

    def verificar(self):
        try:
            int(self.valor_beneficio.get())
            try:
                self.texto_alerta_beneficio.set('')
                int(self.valor_plazo.get())
                self.texto_alerta_plazo.set('')
                self.ingresar_datos_base()
            except ValueError:
                self.texto_alerta_plazo.set('Ingrese un valor correcto')
        except ValueError:
            self.texto_alerta_beneficio.set('Ingrese un valor correcto')
        

    def ingresar_datos_base(self):
        tarea = Tareas(int(self.valor_beneficio.get()), int(self.valor_plazo.get()))
        if self.id_tarea == None:
            ingresar_tarea(tarea)
        else:
            editar_tarea(tarea, self.id_tarea)
        self.ingresar_datos_tabla()

    def editar_datos(self):
        try:
            self.id_tarea = int(self.tabla.item(self.tabla.selection())['values'][0])
            beneficio_tarea = self.tabla.item(self.tabla.selection())['values'][1]
            plazo_tarea = self.tabla.item(self.tabla.selection())['values'][2]

            self.valor_beneficio.set(beneficio_tarea)
            self.valor_plazo.set(plazo_tarea)
            self.id_tarea = None
        except:
            messagebox.showinfo(title='Editar registro', message='No ha seleccionado un registro')

    def eliminar_datos(self):
        try:
            self.id_tarea = int(self.tabla.item(self.tabla.selection())['values'][0])
            eliminar_tarea(self.id_tarea)
            self.ingresar_datos_tabla()
            self.id_tarea = None
        except:
            messagebox.showinfo(title='Eliminar registro', message='No ha seleccionado un registro')

    def ingresar_datos_tabla(self):
        self.lista_tareas = listar_en_tabla()
        self.tabla.delete(*self.tabla.get_children())
        for tarea in self.lista_tareas:
            self.tabla.insert(parent='',index='end', text="", values= (tarea[0], tarea[1], tarea[2]))

    def resetear_datos(self):
        tarea1 = Tareas(50,2)
        tarea2 = Tareas(10,1)
        tarea3 = Tareas(15,2)
        tarea4 = Tareas(30,1)

        borrar_tabla_tareas()
        crear_tabla_tareas()
        ingresar_tarea(tarea1)
        ingresar_tarea(tarea2)
        ingresar_tarea(tarea3)
        ingresar_tarea(tarea4)
        self.ingresar_datos_tabla()
        

    def init_widgets(self):

        # label para el titulo
        tk.Label(self,
                 text="Ingreso de tareas",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.X, pady=30)

        # frame donde se colocaran label y entry para datos que ingresa el usuario
        input_frame = tk.Frame(self, background=style.BG)
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(2, weight=1)
        input_frame.columnconfigure(3, weight=1)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH)

        # label beneficio
        tk.Label(input_frame,
                 text='Beneficio',
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0, pady=(20, 0), padx=(0, 5), sticky=tk.E)

        # label plazo
        tk.Label(input_frame,
                 text='Plazo',
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=2, pady=(20, 0), padx=(0, 5), sticky=tk.E)

        # entry para el valor de beneficio
        borde_entry_1 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_1.grid(row=0, column=1, pady=(30, 0), padx=0, sticky=tk.W)

        self.valor_beneficio = tk.StringVar()
        entry_valor_beneficio = tk.Entry(borde_entry_1,
                                         textvariable=self.valor_beneficio,
                                         **style.STYLE_ENTRY,
                                         width=6,
                                         )
        entry_valor_beneficio.pack(side=tk.TOP, fill=tk.X, expand=True)

        canvas_linea_1 = tk.Canvas(
            borde_entry_1, **style.STYLE_CANVAS, width=250)
        canvas_linea_1.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_1.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        self.texto_alerta_beneficio = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_beneficio,
                 **style.STYLE_WARNING,
                 ).pack()

        # entry para el valor de plazo
        borde_entry_2 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_2.grid(row=0, column=3, pady=(30, 0), padx=0, sticky=tk.W)

        self.valor_plazo = tk.StringVar()
        entry_valor_plazo = tk.Entry(borde_entry_2,
                                     textvariable=self.valor_plazo,
                                     **style.STYLE_ENTRY,
                                     width=6,
                                     )
        entry_valor_plazo.pack(side=tk.TOP, fill=tk.X, expand=True)

        canvas_linea_2 = tk.Canvas(
            borde_entry_2, **style.STYLE_CANVAS, width=250)
        canvas_linea_2.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_2.create_line(0, 0, 250, 0, **style.STYLE_CANVAS_LINE)

        self.texto_alerta_plazo = tk.StringVar()
        tk.Label(borde_entry_2,
                 textvariable=self.texto_alerta_plazo,
                 **style.STYLE_WARNING,
                 ).pack()

        btn_frame = tk.Frame(self, background=style.BG)
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)
        btn_frame.columnconfigure(2, weight=1)
        btn_frame.columnconfigure(3, weight=1)
        btn_frame.pack(side=tk.TOP, fill=tk.X)

        # boton para nuevo elemento (desbloquear campos)
        borde_entry_6 = tk.LabelFrame(btn_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_6.grid(row=1, column=0, pady=(20, 0))

        borde_4 = tk.LabelFrame(borde_entry_6, **style.STYLE_BUTTON_BORDER)
        borde_4.pack()

        boton_desbloqueo = tk.Button(borde_4,
                                     text="Resetear",
                                     **style.STYLE_BUTTON,
                                     command=self.resetear_datos,
                                     )
        boton_desbloqueo.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_desbloqueo.bind('<Enter>', event.on_enter)
        boton_desbloqueo.bind('<Leave>', event.on_leave)

        # boton para ingresar
        borde_entry_3 = tk.LabelFrame(btn_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_3.grid(row=1, column=1, pady=(20, 0))

        borde_1 = tk.LabelFrame(borde_entry_3, **style.STYLE_BUTTON_BORDER)
        borde_1.pack()

        boton_ingreso = tk.Button(borde_1,
                                  text="Ingresar",
                                  **style.STYLE_BUTTON,
                                  command=self.verificar,
                                  )
        boton_ingreso.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_ingreso.bind('<Enter>', event.on_enter)
        boton_ingreso.bind('<Leave>', event.on_leave)

        # boton para editar
        borde_entry_4 = tk.LabelFrame(btn_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_4.grid(row=1, column=2, pady=(20, 0))

        borde_2 = tk.LabelFrame(borde_entry_4, **style.STYLE_BUTTON_BORDER)
        borde_2.pack()

        boton_editar = tk.Button(borde_2,
                                 text="Editar",
                                 **style.STYLE_BUTTON,
                                 command=self.editar_datos,
                                 )
        boton_editar.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_editar.bind('<Enter>', event.on_enter)
        boton_editar.bind('<Leave>', event.on_leave)

        # boton para eliminar
        borde_entry_5 = tk.LabelFrame(btn_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_5.grid(row=1, column=3, pady=(20, 0))

        borde_3 = tk.LabelFrame(borde_entry_5, **style.STYLE_BUTTON_BORDER)
        borde_3.pack()

        boton_eliminar = tk.Button(borde_3,
                                   text="Eliminar",
                                   **style.STYLE_BUTTON,
                                   command=self.eliminar_datos,
                                   )
        boton_eliminar.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_eliminar.bind('<Enter>', event.on_enter)
        boton_eliminar.bind('<Leave>', event.on_leave)

        # tabla para representar las tareas que han sido ingresadas
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
