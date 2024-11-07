import reflex as rx
import os  
import supabase
import dotenv
from ..NavBar.navbar import navbar
class Supabase():
    dotenv.load_dotenv()
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    supabase = supabase.Client(SUPABASE_URL, SUPABASE_KEY)

    def get_recetas(self) -> list[dict]:

        response = self.supabase.table("recetas").select("*").execute()
        recetas_data: list[dict] = []
        if len(response.data) > 0:
            for item in response.data:
                    recetas_data.append({"id":item["id"],'nombre_receta':item['nombre_receta'],
            'ingredientes':item['ingredientes'], 'procedimientos':item['procedimientos'], 'imagen':item['imagen']})
        return recetas_data
    def add_receta(self, nombre_receta: str, ingredientes: str, procedimientos: str, imagen: str):
        response = self.supabase.table("recetas").insert({
            "nombre_receta": nombre_receta,
            "ingredientes": ingredientes,
            "imagen": imagen,
            "procedimientos": procedimientos
        }).execute()
    def borrar_receta_supabase(self, id:int):
        response = self.supabase.table("recetas").delete().eq("id", id).execute()
        print(response, id)
        return response
supabase = Supabase()
async def recetas() -> list[dict]:
    return supabase.get_recetas()
class StateSubmit(rx.State):
    recetaaaas: list[dict] = []
    nombre_receta: str = ""
    ingredientes: str = ""
    procedimientos: str = ""
    imagen: str = ""
    id: int = 0
    recetas_filtradas: list[dict] = []
    busqueda_recetas=str = ""


##INTENTO DE POST###########################################
    async def receta(self):
        self.recetaaaas = await recetas()

    def borrar_receta(self,id: int):
        self.id = id
        supabase.borrar_receta_supabase(self.id)
        self.recetaaaas = supabase.get_recetas()
        self.id = 0
        print(self.id)

    async def submit_receta(self):
        supabase.add_receta(self.nombre_receta, self.ingredientes, self.procedimientos, self.imagen)
        await self.receta()
        self.nombre_receta = ""
        self.ingredientes = ""
        self.procedimientos = ""
        self.imagen = ""
    @rx.event
    def buscar_recetas(self):
        if self.busqueda_recetas == "":
            self.recetaaaas = supabase.get_recetas()
        else:
            busqueda = self.busqueda_recetas.lower()
            self.recetaaaas = list(filter(lambda receta: busqueda in receta.get("nombre_receta").lower(), self.recetaaaas))
        print("Recetas filtradas:", self.recetaaaas)
    
    def set_busqueda_recetas(self, valor):
        # Actualiza el término de búsqueda y filtra recetas
        self.busqueda_recetas = valor
        self.buscar_recetas()
def misrecetas() -> rx.Component:
    return rx.box(
        navbar(),
        rx.flex(
            rx.box(
            # Formulario para agregar una nueva receta
            rx.flex(
                rx.text("Agregar nueva receta",
                    size = "6",
                    color = "#556b2f",
                    text_shadow = "1px 1px 1px black"),
                justify = "center",
                margin = "10px"),
            rx.input(placeholder="Nombre de la receta",
                value=StateSubmit.nombre_receta,
                on_change=StateSubmit.set_nombre_receta,
                width = "20rem",
                height = "2.5rem",
                margin = "1rem"),
            rx.input(placeholder="Ingredientes",
                value=StateSubmit.ingredientes,
                on_change=StateSubmit.set_ingredientes,
                width = "20rem",
                height = "2.5rem",
                margin = "1rem"),
            rx.input(placeholder="Imagen",
                value=StateSubmit.imagen,
                on_change=StateSubmit.set_imagen,
                width = "20rem",
                height = "2.5rem",
                margin = "1rem"),
            rx.text_area(placeholder="Procedimientos",
                value=StateSubmit.procedimientos,
                on_change=StateSubmit.set_procedimientos,
                rows= "10",
                widht = "20",
                margin = "1rem"),
            rx.flex(
                rx.button("Agregar receta",
                type="submit",
                on_click=lambda: [
                StateSubmit.submit_receta,
                rx.toast("Receta Cargada Correctamente",
                    position="top-right", 
                    style={"background-color": "green",
                        "color": "white",
                        "border": "1px solid green",
                        "border-radius": "0.53m"},)]),
            justify="center",
            align="center",
            margin = "1rem")
            ),
        justify="center",
        align="center",
        flex_direction="column"
        ),
        rx.divider(),
        rx.flex(
            rx.input(placeholder="Buscar receta...",
                value=StateSubmit.busqueda_recetas,
                on_change=StateSubmit.set_busqueda_recetas,
                width = "20rem",
                height = "2.5rem",
                margin = "1rem",
            ),justify="center",
            align="center",),
        # rx.button("Buscar", on_click=StateSubmit.buscar_recetas),

        #rx.button("Buscar", on_click=StateSubmit.buscar_recetas),

        #rx.button("log", on_click=lambda: rx.console_log(StateSubmit.recetaaaas)),
        rx.grid(
            rx.foreach(StateSubmit.recetaaaas, lambda item:
                rx.flex(rx.card(
                        rx.text(item["nombre_receta"], color="white", size="6"),
                        rx.image(
                            src=item['imagen'],
                            width="100px",
                            height="100px",
                            fit="cover",
                        ),
                        rx.button(item['ingredientes']),
                        rx.text(item['procedimientos'], color="blue"),
                        rx.button(f"Borrar", on_click=lambda:[
                            StateSubmit.borrar_receta(item['id']), 
                            rx.toast("Receta Borrada Correctamente", position="top-right", 
                                    style={
                                    "background-color": "green",
                                    "color": "white",
                                    "border": "1px solid green",
                                    "border-radius": "0.53m",
                                    }, ) ]),
                        height="20rem", width="30rem" 
                ),margin="13px")
                
        ), columns="4",
    spacing="4",

    width="100%", ),
    
                width="100%",
                    min_height="100vh",

        )

