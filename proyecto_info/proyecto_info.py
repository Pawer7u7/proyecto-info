import reflex as rx
from .NavBar.navbar import navbar
from .Recetas.recetas import recetasss
from .Mis_Recetas.misrecetas import misrecetas, StateSubmit

def index() -> rx.Component:
    return rx.box(
        navbar(),  
            rx.flex(
                rx.flex(
                    rx.text(
                        "Comarca Code Recetas App",
                        font_size="8rem",
                        color="#556b2f",
                        text_shadow="1px 1px 1px black"
                    ),
                    rx.text("""Nuestro proyecto se trata sobre una página de recetas en la cual el usuario busca a traves de distintas especificaciones, su receta deseada. 
                        La página se realizó con reflex el cual es un framework (plantilla que sirve para desarrollar un proyecto)
                        de python de codigo abierto que permite crear aplicaciones web full-stack.""",
                        color ="#556b2f",
                        font_size="2em",
                        text_align="center",
                        style={"display": "flex",
                            "justifyContent": "center",
                            "alignItems": "center",
                            "height": "100vh"}
                    ),
                    justify="center",
                    align="center",
                    width="100%",
                    flex_direction = "column"
                ),width="100%",
                    background_color="#eee5e9",
                    height="100vh",),
                
            width="100%"
            ),
app = rx.App()
app.add_page(index)
app.add_page(recetasss)
app.add_page(misrecetas, on_load=StateSubmit.receta())
app._compile