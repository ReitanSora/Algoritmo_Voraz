from static import style

# eventos para efecto de hover en botones
def on_enter(e):
    e.widget.config(**style.STYLE_BUTTON_ENTER)


def on_leave(e):
    e.widget.config(**style.STYLE_BUTTON)

    
def on_enter_nav(e):
    e.widget.config(**style.STYLE_BUTTON_NAV_ENTER)


def on_leave_nav(e):
    e.widget.config(**style.STYLE_BUTTON_NAV)
