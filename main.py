import flet as ft


def main(page: ft.Page):

    def form_objetive_1(page):
        page.controls.clear()
        page.controls.append(ft.Column([
            ft.Text("Formulario de Paciente", style=ft.TextStyle(size=20, weight="bold")),
            ft.TextField(label="Nombre"),
            ft.TextField(label="Apellido"),
            ft.ElevatedButton(text="Guardar", on_click=save_form),
            ft.ElevatedButton(text="Regresar", on_click=show_main_screen)
        ], spacing=10, alignment="center"))
        page.update()

    def form_objetive_2(page):
        page.controls.clear()
        page.controls.append(ft.Column([
            ft.Text("Otro Formulario", style=ft.TextStyle(size=20, weight="bold")),
            ft.TextField(label="Nombre 2"),
            ft.TextField(label="Apellido 2"),
            ft.ElevatedButton(text="Guardar", on_click=save_form),
            ft.ElevatedButton(text="Regresar", on_click=show_main_screen)
        ], spacing=10, alignment="center"))
        page.update()

        
    def form_objetive_3(page):
        page.controls.clear()
        page.controls.append(ft.Column([
            ft.Text("Otro Formulario", style=ft.TextStyle(size=20, weight="bold")),
            ft.TextField(label="Campo 1"),
            ft.TextField(label="Campo 2"),
            ft.ElevatedButton(text="Guardar", on_click=save_form),
            ft.ElevatedButton(text="Regresar", on_click=show_main_screen)
        ], spacing=10, alignment="center"))
        page.update()
    
    def show_form(form_id, e):
        if form_id == "form_1":
            form_objetive_1(page)
        elif form_id == "form_2":
            form_objetive_2(page)
        elif form_id == "form_3":
            form_objetive_3(page)
        else:
            print(f"Formulario con ID {form_id} no encontrado")

    def save_form(e):
        # Aquí puedes agregar la lógica para guardar la información del paciente
        page.controls.clear()
        page.controls.append(ft.Column([
            ft.Text("Formulario enviado correctamente.", style=ft.TextStyle(size=20, weight="bold")),
            ft.ElevatedButton(text="Regresar", on_click=show_main_screen)
        ], spacing=10, alignment="center"))
        page.update()
        
    def show_main_screen(e=None):
        page.controls.clear()
        cards = [
            create_card("Objetivo 1", "Nombre 1", "form_1"),
            create_card("Objetivo 2", "Nombre 2", "form_2"),
            create_card("Objetivo 3", "Nombre 3", "form_3")
        ]
        page.controls.append(ft.Column(cards, alignment="center", horizontal_alignment="center", spacing=20))
        page.update()
    
    def create_card(objetivo, nombre, form_id):
        return ft.Container(
            content=ft.Column([
                ft.Text(objetivo, style=ft.TextStyle(size=16, weight="bold", color=ft.colors.BLUE_500)),
                ft.Text(nombre, style=ft.TextStyle(size=14, color=ft.colors.GREY_500)),
                ft.ElevatedButton(
                text="Abrir Formulario",
                on_click=lambda e: show_form(form_id,e)
            )
            ], spacing=10, alignment="center"), 
    
            padding=20,
            border_radius=15,
            # shadow=ft.BoxShadow(
            #     offset=ft.Offset(2, 2),   
            #     blur_radius=10,
            #     spread_radius=1,
            #     color=ft.colors.GREY_500
            # ), 
            bgcolor=ft.colors.WHITE,
            margin=10
        )
        
    page.title = "Aplicación de Flet"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    #cards = [
    #    create_card("Objetivo 1", "Nombre 1"),
    #    create_card("Objetivo 2", "Nombre 2"),
    #    create_card("Objetivo 3", "Nombre 3")
    #]

    cards = [
        create_card("Objetivo 1", "Nombre 1", "form_1"),
        create_card("Objetivo 2", "Nombre 2", "form_2"),
        create_card("Objetivo 3", "Nombre 3", "form_3")
    ]


    page.add(ft.Column(cards, alignment="center", horizontal_alignment="center", spacing=20))
    page.update()

ft.app(target=main)