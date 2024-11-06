import reflex as rx
from .NavBar.navbar import navbar
from .Recetas.recetas import recetasss
from .Mis_Recetas.misrecetas import misrecetas, StateSubmit

def index(recetass: list = []) -> rx.Component:
    return rx.box(
        navbar(),
        # add_receta(),   
                rx.flex(rx.flex(
                    rx.text("Comarca Code Recetas App", font_size="8rem", color="#556b2f", text_shadow="1px 1px 1px black"),
                    justify_content="center",
                    align_content="center",
                    width="100%"
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