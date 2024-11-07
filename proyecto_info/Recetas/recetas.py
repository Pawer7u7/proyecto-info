import reflex as rx
from ..NavBar.navbar import navbar
import requests
import math

class State_recetas(rx.State):
    receta: list[dict] = []   
    searchInput: str = ""
    loading: bool = False
    @rx.event
    def set_searchInput(self, value: str):
        self.searchInput = value
    @rx.event
    def get_recetas(self):
        self.receta = []
        response = requests.get(f"https://api.edamam.com/api/recipes/v2?type=public&q={self.searchInput}&app_id=7f24909e&app_key=2a4122809b5331157cb1d4d18bb18823")
        recetasdata=[]
        recetasdata = response.json()['hits']
        print(State_recetas.searchInput)
        # print("Datos recibidos:", recetasdata)
        for recipe in recetasdata:
            self.receta.append({'name': recipe['recipe']['label'],
            'url':str(recipe['recipe']['url']),
            'ingredients': recipe['recipe']['ingredientLines'],
            'calories': float(recipe['recipe']['calories']),
            'image': recipe['recipe']['image']})
        self.searchInput = ""
        #print(type(self.receta[0]['url']))
        # print(self.receta)
        # return self.receta
        # return recetasdata
def recetasss() -> rx.Component:
        return rx.box(navbar(),
            rx.flex(rx.flex(
                    rx.text("Recetas", font_size="5rem", color="#556b2f", text_shadow="1px 1px 1px black"),
                    rx.text("Ingrese el nombre de una receta o ingrediente para buscar",color="#556b2f"),
                justify="center",
                align="center",
                flex_direction="column",
            ),
                rx.flex(
                    
                    rx.input(
                placeholder="Buscar receta...",
                value=State_recetas.searchInput,
                on_change=State_recetas.set_searchInput
            ),
            rx.button("Buscar", on_click=lambda:
                            [State_recetas.set_loading(True),
                                State_recetas.get_recetas,
                                State_recetas.set_loading(False)
                                ]),
                #rx.button("Recetas", on_click=lambda: rx.console_log(State_recetas.receta)),
                #rx.button("url", on_click=lambda: rx.console_log(State_recetas.receta[0]['url'])),

                    justify_content="center",
                    align_content="center",
                    width="100%"
                ),rx.cond(State_recetas.loading,
                    rx.flex( 
                        rx.button(
                                rx.spinner(loading=True), "CARGANDO RECETAS", disabled=True, size="3",color="black"
                                    ),justify="center",)
                
                    ),
                    rx.grid(rx.foreach(State_recetas.receta, lambda item:
                rx.card(
                    rx.vstack( rx.text(item['name'], color="#556b2f", size="6",weight="bold"),
                    #rx.link("link",href=item['url']),
                    rx.image(
                        src=item['image'],
                        width="200px",
                        height="200px",
                        fit="cover",
                    ),
                    rx.flex(
                        rx.text("Ingredientes: " ,color="black", size="4", weight="medium"),
                        rx.text(item["ingredients"], color="black",),
                        flex_direction="column",
                        ),
                    
                    rx.text(f"Calorías: {(item['calories'])}", color="black", size="4", weight="medium"),
                    rx.flex(  rx.text("Ver Receta: " ,color="black", size="4", weight="medium"),
                        rx.text(item["url"], color="black",),
                        flex_direction="column",),
                    justify_content="center",
                    ),
                
                    margin="15px",
                    justify_content="center",
                    variant="classic"
            ),),
            columns="4",
            spacing="4"
            ),
                width="100%",
                    background_color="#eee5e9",
                    min_height="100vh",
                    flex_direction="column",),
            
            
            ),
