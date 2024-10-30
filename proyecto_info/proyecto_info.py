import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.text("Hola asdasd")

app = rx.App()
app.add_page(index)
app._compile