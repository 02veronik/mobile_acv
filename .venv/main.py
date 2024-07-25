import flet as ft


def main(page: ft.Page):

    def show_form(e):
        page.controls.clear()
        page.controls.append(ft.Column([
            ft.Text("Formulario de Paciente", style=ft.TextStyle(size=20, weight="bold")),
            ft.TextField(label="Nombre"),
            ft.TextField(label="Apellido"),
            ft.ElevatedButton(text="Guardar", on_click=save_form)
        ]))
        page.update()

    def save_form(e):
        # Aquí puedes agregar la lógica para guardar la información del paciente
        page.controls.clear()
        page.controls.append(ft.Text("Formulario enviado correctamente.", style=ft.TextStyle(size=20, weight="bold")))
        page.update()
    
    def create_card(objetivo, nombre):
        return ft.Card(
            content=ft.Column([
                ft.Text(objetivo, style=ft.TextStyle(size=16, weight="bold")),
                ft.Text(nombre, style=ft.TextStyle(size=14)),
                ft.ElevatedButton(text="Abrir Formulario", on_click=show_form)
            ])
        )
    page.title = "Aplicación de Flet"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    cards = [
        create_card("Objetivo 1", "Nombre 1"),
        create_card("Objetivo 2", "Nombre 2"),
        create_card("Objetivo 3", "Nombre 3")
    ]

    page.add(ft.Column(cards, alignment="center", horizontal_alignment="center", spacing=20))
    page.update()

ft.app(target=main)