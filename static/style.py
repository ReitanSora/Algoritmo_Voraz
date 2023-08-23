
BG = "#292D3E"

COLOR_TITULO = "#FEFFEA"
COLOR_SUBTITULO = "#FEFFEA"

COLOR_BLANCO = "#FFF"
COLOR_NEGRO = "#000"
COLOR_GRIS = "#C2C2C2"
COLOR_AQUA = "#257dca"
COLOR_AQUA_OSCURO = "#1D6AAD"
COLOR_MAGENTA_NORMAL = "#512BCF"
COLOR_MAGENTA_CLARO = "#8A67FF"
COLOR_MAGENTA_OSCURO = "#3b1f98"
COLOR_CIAN = "#FF6B6B"

STYLE_TITTLE = {
    "font": ("Corbel", 20, "bold"),
    "bg": BG,
    "fg": COLOR_TITULO
}

STYLE_SUBTITTLE = {
    "font": ("Corbel", 14, "bold"),
    "bg": BG,
    "fg": COLOR_SUBTITULO,
}

STYLE_TEXT = {
    "font": ("Corbel", 14, ""),
    "bg": BG,
    "fg": COLOR_SUBTITULO,
    "wraplength": "700p",
    "justify": "left",
}

STYLE_WARNING = {
    "font": ("Corbel", 9, "bold"),
    "bg": BG,
    "fg": COLOR_GRIS,
}

STYLE_ENTRY_BORDER = {
    "font": ("Corbel", 14, "bold"),
    "bg": BG,
    "fg": COLOR_GRIS,
    "bd": 0,
    "relief": "flat",
}

STYLE_BUTTON_BORDER = {
    "bg": COLOR_MAGENTA_CLARO,
    "relief": "flat",
    "bd": 3,
    "width": 12,
}

STYLE_BUTTON = {
    "font": ("Corbel", 14, "bold"),
    "bg": COLOR_BLANCO,
    "fg": COLOR_MAGENTA_CLARO,
    "activeforeground": COLOR_BLANCO,
    "activebackground": COLOR_MAGENTA_NORMAL,
    "relief": "sunken",
    "cursor": "hand2",
    "bd": 0,
    "width": 10,
    "padx": 20,
}

STYLE_BUTTON_TOOLBAR = {
    "bg": COLOR_MAGENTA_CLARO,
    "activebackground": COLOR_BLANCO,
    "highlightbackground": COLOR_MAGENTA_CLARO,
    "highlightcolor": COLOR_MAGENTA_CLARO,
    "relief": "flat",
    "cursor": "hand2",
    "bd": 0,
    "anchor": "center",
}

STYLE_BUTTON_NAV = {
    "font": ("Corbel", 12, "bold"),
    "bg": COLOR_MAGENTA_CLARO,
    "fg": COLOR_BLANCO,
    "activeforeground": COLOR_BLANCO,
    "activebackground": COLOR_MAGENTA_NORMAL,
    "relief": "sunken",
    "cursor": "hand2",
    "bd": 0,
    "padx": 20,
    "pady": 10,
}

STYLE_BUTTON_ENTER = {
    "bg": COLOR_MAGENTA_CLARO,
    "fg": COLOR_BLANCO,
}

STYLE_BUTTON_NAV_ENTER = {
    "bg": COLOR_MAGENTA_NORMAL,
    "fg": COLOR_BLANCO
}

STYLE_ENTRY = {
    "font": ("Corbel", 14),
    "bg": BG,
    "fg": COLOR_TITULO,
    "bd": 0,
    "selectbackground": COLOR_BLANCO,
    "selectforeground": COLOR_MAGENTA_NORMAL,
    "justify": "center"
}

STYLE_ENTRY_DES = {
    "font": ("Verdana", 14),
    "bg": BG,
    "fg": COLOR_BLANCO,
    "bd": 0,
    "selectbackground": COLOR_BLANCO,
    "selectforeground": COLOR_MAGENTA_NORMAL,
    "readonlybackground": BG,
    "cursor": "",
    "state": "readonly",
    "justify": "center"
}

STYLE_RADIO_BUTTON = {
    "font": ("Corbel", 14, "bold"),
    "bg": BG,
    "fg": COLOR_BLANCO,
    "activebackground": BG,
    "activeforeground": COLOR_MAGENTA_CLARO,
    "selectcolor": BG,
    "border": "0",
    "anchor": "center",
    "borderwidth": "0",
    "relief": "flat"
}

STYLE_CANVAS = {
    "bg": BG,
    "height": 3,
    "bd": 0,
    "relief": "flat",
    "highlightthickness": 0
}

STYLE_CANVAS_TOGGLE = {
    "bg": BG,
    "height": 29,
    "bd": 0,
    "relief": "flat",
    "highlightthickness": 0
}

STYLE_CANVAS_LINE = {
    "width": "3",
    "fill": COLOR_MAGENTA_CLARO
}

STYLE_MENU_BAR = {
    "tearoff": 0,
    "font": ("Ubuntu", 11),
    "activebackground": COLOR_MAGENTA_CLARO,
    "bd": -2,
}
