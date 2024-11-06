import reflex as rx

def navbar() -> rx.Component:
    return rx.flex(
               rx.stack(
                    rx.box(
                        rx.link(rx.button("Home",variant="soft", color="white",background_color="#556b2f",_hover={
        "opacity": 0.7,
    }), href="/"),
                    ),          
                    rx.box(
                         rx.link(rx.button("Recetas",variant="soft", color="white",background_color="#556b2f",_hover={
        "opacity": 0.7,
    }), href="/recetasss")),
                    rx.box(
                         rx.link(rx.button("Mis Recetas",variant="soft", color="white",background_color="#556b2f",_hover={
        "opacity": 0.7,
    }), href="/misrecetas")
                        ),
                        height="5rem",
                        align="center",
                        gap="9rem"
                    ),             
        position="sticky",
        top="0",
        background_color="#f1bf98",
        justify_content="center",
        align_content="center",
        flex_direction="row",
        width="100%",
        z_index="100",
)

  