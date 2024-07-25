import flet as ft


def main(page: ft.Page):

    # Formulario 01
    def form_objetive_1(page):
        page.controls.clear()
        page.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Formulario de Predicción", style=ft.TextStyle(size=20, weight="bold")),
                    
                    # Género
                    ft.Row([
                        ft.Text("Género"),
                        ft.Dropdown(
                            options=[
                                ft.dropdown.Option("", "Seleccionar opción"),
                                ft.dropdown.Option("0", "Femenino"),
                                ft.dropdown.Option("1", "Masculino")
                            ]
                           # value="",  # Valor por defecto
                          #  required=True
                        )
                    ], alignment="center"),
                    
                    # Edad
                    ft.Row([
                        ft.Text("Edad"),
                        ft.TextField(
                            label="Edad",
                            keyboard_type="number"
                            #required=True
                        )
                    ], alignment="center"),

                    # Tipo de Trabajo
                    ft.Row([
                        ft.Text("Tipo de Trabajo"),
                        ft.Dropdown(
                            options=[
                                ft.dropdown.Option("", "Seleccionar opción"),
                                ft.dropdown.Option("1", "Trabajador por cuenta propia"),
                                ft.dropdown.Option("2", "Trabajador para el gobierno"),
                                ft.dropdown.Option("3", "Nunca trabajó"),
                                ft.dropdown.Option("4", "Trabajador privado")
                            ],
                            value=""  # Valor por defecto
                           # required=True
                        )
                    ], alignment="center"),
                    
                    # Hipertensión
                    ft.Row([
                        ft.Text("Hipertensión"),
                        ft.Dropdown(
                            options=[
                                ft.dropdown.Option("", "Seleccionar opción"),
                                ft.dropdown.Option("0", "No"),
                                ft.dropdown.Option("1", "Sí")
                            ],
                            value=""  # Valor por defecto
                            #required=True
                        )
                    ], alignment="center"),
                    
                    # Cardiopatía
                    ft.Row([
                        ft.Text("Cardiopatía"),
                        ft.Dropdown(
                            options=[
                                ft.dropdown.Option("", "Seleccionar opción"),
                                ft.dropdown.Option("0", "No"),
                                ft.dropdown.Option("1", "Sí")
                            ],
                            value=""  # Valor por defecto
                            #required=True
                        )
                    ], alignment="center"),
                    
                    # Nivel de Glucosa Promedio
                    ft.Row([
                        ft.Text("Nivel de Glucosa Promedio"),
                        ft.TextField(
                            label="Nivel de Glucosa Promedio",
                            keyboard_type="number"
                            #required=True
                        )
                    ], alignment="center"),
                    
                    # ICM
                    ft.Row([
                        ft.Text("ICM"),
                        ft.TextField(
                            label="ICM",
                            keyboard_type="number"
                            #required=True
                        )
                    ], alignment="center"),
                    
                    # Estado de Fumador
                    ft.Row([
                        ft.Text("Estado de Fumador"),
                        ft.Dropdown(
                            options=[
                                ft.dropdown.Option("", "Seleccionar opción"),
                                ft.dropdown.Option("1", "Anteriormente fumó"),
                                ft.dropdown.Option("2", "Nunca fumó"),
                                ft.dropdown.Option("3", "Fuma")
                            ],
                            value=""  # Valor por defecto
                            #required=True
                        )
                    ], alignment="center"),
                    
                    # Botones
                    ft.Row([
                        ft.ElevatedButton(text="Guardar", on_click=save_form),
                        ft.ElevatedButton(text="Regresar", on_click=show_main_screen)
                    ], spacing=10, alignment="center")
                ],
                spacing=10,
                alignment="center"
            )
        )
        page.update()


    def form_objetive_2(page):
        page.controls.clear()
        page.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Formulario de Predicción", style=ft.TextStyle(size=20, weight="bold")),
                    
                    # Género
                    ft.Row([
                        ft.Text("Género"),
                        ft.Dropdown(
                            options=[
                                ft.dropdown.Option("", "Seleccionar opción"),
                                ft.dropdown.Option("0", "Femenino"),
                                ft.dropdown.Option("1", "Masculino")
                            ]
                           # value="",  # Valor por defecto
                          #  required=True
                        )
                    ], alignment="center"),
                    
                    # Edad
                    ft.Row([
                        ft.Text("Edad"),
                        ft.TextField(
                            label="Edad",
                            keyboard_type="number"
                            #required=True
                        )
                    ], alignment="center"),

                    # Tipo de Trabajo
                    ft.Row([
                        ft.Text("Tipo de Trabajo"),
                        ft.Dropdown(
                            options=[
                                ft.dropdown.Option("", "Seleccionar opción"),
                                ft.dropdown.Option("1", "Trabajador por cuenta propia"),
                                ft.dropdown.Option("2", "Trabajador para el gobierno"),
                                ft.dropdown.Option("3", "Nunca trabajó"),
                                ft.dropdown.Option("4", "Trabajador privado")
                            ],
                            value=""  # Valor por defecto
                           # required=True
                        )
                    ], alignment="center"),
                    
                    # Hipertensión
                    ft.Row([
                        ft.Text("Hipertensión"),
                        ft.Dropdown(
                            options=[
                                ft.dropdown.Option("", "Seleccionar opción"),
                                ft.dropdown.Option("0", "No"),
                                ft.dropdown.Option("1", "Sí")
                            ],
                            value=""  # Valor por defecto
                            #required=True
                        )
                    ], alignment="center"),
                    
                    # Cardiopatía
                    ft.Row([
                        ft.Text("Cardiopatía"),
                        ft.Dropdown(
                            options=[
                                ft.dropdown.Option("", "Seleccionar opción"),
                                ft.dropdown.Option("0", "No"),
                                ft.dropdown.Option("1", "Sí")
                            ],
                            value=""  # Valor por defecto
                            #required=True
                        )
                    ], alignment="center"),
                    
                    # Nivel de Glucosa Promedio
                    ft.Row([
                        ft.Text("Nivel de Glucosa Promedio"),
                        ft.TextField(
                            label="Nivel de Glucosa Promedio",
                            keyboard_type="number"
                            #required=True
                        )
                    ], alignment="center"),
                    
                    # ICM
                    ft.Row([
                        ft.Text("ICM"),
                        ft.TextField(
                            label="ICM",
                            keyboard_type="number"
                            #required=True
                        )
                    ], alignment="center"),
                     
                    
                    # Botones
                    ft.Row([
                        ft.ElevatedButton(text="Guardar", on_click=save_form),
                        ft.ElevatedButton(text="Regresar", on_click=show_main_screen)
                    ], spacing=10, alignment="center")
                ],
                spacing=10,
                alignment="center"
            )
        )
        page.update()

#--------------INICIO FORMULARIO PARA PREDICCIÓN 3     
    def save_form(e):
        # Validar el formulario
        gender_value = gender_select.value
        age_value = age_input.value
        
        if gender_value not in ["0", "1"]:
            error_message.text = "Se requiere seleccionar una opción."
            page.update()
            return

        try:
            age = int(age_value)
            if age <= 0:
                error_message.text = "La edad debe ser un número positivo."
                page.update()
                return
        except ValueError:
            error_message.text = "Valor de edad incorrecto. Debe ser un número positivo."
            page.update()
            return

        # Aquí podrías agregar la lógica para guardar los datos del formulario
        print("Formulario guardado exitosamente")
        show_main_screen(e)  # Volver a la pantalla principal después de guardar
    







    def form_objetive_3(page):
        page.controls.clear()
        page.controls.append(
            ft.Column(
                controls=[
                    ft.Text("Formulario de Predicción", style=ft.TextStyle(size=20, weight="bold")),
                    
                    # Estado de Fumador
                    ft.Row([
                        ft.Text("Estado de Fumador"),
                        ft.Dropdown(
                            options=[
                                ft.dropdown.Option("", "Seleccionar opción"),
                                ft.dropdown.Option("0", "No"),
                                ft.dropdown.Option("1", "Si"), 
                            ],
                            value=""  # Valor por defecto
                            #required=True
                        )
                    ], alignment="center"),
                    
                    # Bebedor frecuente
                    ft.Row([
                        ft.Text("Bebedor frecuente"),
                        ft.Dropdown(
                            options=[
                                ft.dropdown.Option("", "Seleccionar opción"),
                                ft.dropdown.Option("0", "No"),
                                ft.dropdown.Option("1", "Si"), 
                            ],
                            value=""  # Valor por defecto
                            #required=True
                        )
                    ], alignment="center"),
                    
                    # Actividad Física
                    ft.Row([
                        ft.Text("Actividad Física"),
                        ft.Dropdown(
                            options=[
                                ft.dropdown.Option("", "Seleccionar opción"),
                                ft.dropdown.Option("0", "No"),
                                ft.dropdown.Option("1", "Si"), 
                            ],
                            value=""  # Valor por defecto
                            #required=True
                        )
                    ], alignment="center"),
                    
                    # Nivel de Glucosa Promedio
                    ft.Row([
                        ft.Text("Nivel de Glucosa Promedio"),
                        ft.TextField(
                            label="Nivel de Glucosa Promedio",
                            keyboard_type="number"
                            #required=True
                        )
                    ], alignment="center"),
                    
                    # Género
                    ft.Row([
                        ft.Text("Género"),
                        ft.Dropdown(
                            options=[
                                ft.dropdown.Option("", "Seleccionar opción"),
                                ft.dropdown.Option("0", "Femenino"),
                                ft.dropdown.Option("1", "Masculino")
                            ]
                           # value="",  # Valor por defecto
                          #  required=True
                        )
                    ], alignment="center"),
                    
                    # Edad
                    ft.Row([
                        ft.Text("Edad"),
                        ft.TextField(
                            label="Edad",
                            keyboard_type="number"
                            #required=True
                        )
                    ], alignment="center"),

                    # Etnia
                    ft.Row([
                        ft.Text("Etnia"),
                        ft.Dropdown(
                            options=[
                                ft.dropdown.Option("", "Seleccionar opción"),
                                ft.dropdown.Option("0", "Indígena"),
                                ft.dropdown.Option("1", "Asiático"),
                                ft.dropdown.Option("2", "Negro"),
                                ft.dropdown.Option("3", "Hispano"),
                                ft.dropdown.Option("4", "Blanco"),
                                ft.dropdown.Option("4", "Otro"),
                                
                            ],
                            value=""  # Valor por defecto
                           # required=True
                        )
                    ], alignment="center"),
                     
                    
                    
                    # ICM
                    ft.Row([
                        ft.Text("ICM"),
                        ft.TextField(
                            label="ICM",
                            keyboard_type="number"
                            #required=True
                        )
                    ], alignment="center"),
                    
                    
                    
                    # Botones
                    ft.Row([
                        ft.ElevatedButton(text="Guardar", on_click=save_form),
                        ft.ElevatedButton(text="Regresar", on_click=show_main_screen)
                    ], spacing=10, alignment="center")
                ],
                spacing=10,
                alignment="center"
            )
        )
        page.update()


    





#---------------FIN FORMULARIO PARA PREDICCIÓN 3 
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