from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class DiagnosticoApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        bienvenida = Label(
            text="Bienvenido a la aplicación de diagnóstico"
        )

        nombre_organizacion = TextInput(
            hint_text="Nombre de organización",
            multiline=False
        )

        boton_confirmar = Button(
            text="Confirmar"
        )

        layout.add_widget(bienvenida)
        layout.add_widget(nombre_organizacion)
        layout.add_widget(boton_confirmar)

        return layout


DiagnosticoApp().run()