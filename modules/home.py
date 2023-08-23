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
from static import style


class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller
        self.init_widgets()


    def init_widgets(self):

        self.container = tk.Canvas(
            self, background=style.BG, bd=0, relief="flat", highlightthickness=0)
        self.container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)


        container_frame = tk.Frame(self.container, background=style.BG)
        container_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.container.create_window((0, 0), window=container_frame)


        # label titulo bienvenida
        tk.Label(
            container_frame,
            text="\n\nEste programa ha sido diseñado en base a la técnica de diseño de algoritmos voraces, ordenamiento, etc, la finalidad de esta herramienta es meramente educativa. Esperamos que este aplicativo sea de utlidad para quien lo necesite.",
            **style.STYLE_TEXT,
        ).pack(side=tk.TOP, fill=tk.X, pady=(0, 20))

        info_frame = tk.Frame(container_frame, background=style.BG)
        info_frame.columnconfigure(0, weight=1)
        info_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=20)

        tk.Label(info_frame,
                 text="Temas incluidos:\n\n     • Ingreso de tareas\n     • Problema de asignación de tareas\n",
                 **style.STYLE_TEXT,
                 ).grid(row=0, column=0, sticky=tk.NW, pady=(0,20))

        tk.Label(info_frame,
                 text="Librerías usadas:\n\n     • tkinter\n     • os\n     • sqlite3\n\n",
                 **style.STYLE_TEXT,
                 ).grid(row=1, column=0, sticky=tk.NW)
        
        tk.Label(info_frame,
                 text="Desarrollado por:\n\n     • Stiven Pilca\n     • Juan Tulcanaza\n",
                 **style.STYLE_TEXT,
                 ).grid(row=2, column=0, sticky=tk.NW)
        
        tk.Label(info_frame,
                 text="Materia:\n\n     • Algoritmos",
                 **style.STYLE_TEXT,
                 ).grid(row=3, column=0, sticky=tk.NW)
        
        tk.Label(info_frame,
                 text="\n\n©Todos los derechos reservados - Universidad Central del Ecuador - 2023\n\n",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=4, column=0)

        self.scroll = tk.Scrollbar(self,
                                   border=0,
                                   orient="vertical",
                                   command=self.container.yview,
                                   )
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.container.configure(yscrollcommand=self.scroll.set)
        self.container.bind('<Configure>', lambda e: self.container.configure(
            scrollregion=self.container.bbox(tk.ALL)))