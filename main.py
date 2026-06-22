from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem

# Ajustamos el tamaño de la ventana para simular la vista apaisada
Window.size = (850, 450)

# Interfaz gráfica en lenguaje KV
KV = '''
<BotonCalc@MDRaisedButton>:
    font_size: "24sp"
    # El último valor (0.85) es la opacidad. Hace el botón ligeramente transparente.
    md_bg_color: 0.25, 0.1, 0.4, 0.85  
    text_color: 1, 1, 1, 1
    size_hint: 1, 1
    elevation: 2

MDFloatLayout:
    
    # --- IMAGEN DE FONDO ---
    # AsyncImage carga la imagen directamente desde internet
    AsyncImage:
        source: "https://i.pinimg.com/736x/e0/92/99/e092998644ad57af9f1d93bbe4332635.jpg"
        allow_stretch: True
        keep_ratio: False
        size_hint: 1, 1
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    # --- CONTENEDOR PRINCIPAL SUPERPUESTO ---
    MDBoxLayout:
        orientation: 'vertical'
        # Un filtro oscuro casi invisible sobre toda la pantalla para mejorar la lectura
        md_bg_color: 0.1, 0.0, 0.2, 0.3  

        # --- ENCABEZADO (Título Centrado) ---
        MDBoxLayout:
            size_hint_y: 0.15
            padding: "10dp"
            
            MDLabel:
                text: "Kuromi Calculadora"
                font_style: "H3"
                theme_text_color: "Custom"
                text_color: 1, 0.7, 0.9, 1  # Rosa claro
                halign: "center"
                valign: "center"

        # --- PANTALLA DE RESULTADOS ---
        MDBoxLayout:
            size_hint_y: 0.2
            padding: ["20dp", "0dp", "20dp", "10dp"]
            
            MDCard:
                md_bg_color: 0.18, 0.08, 0.3, 0.7  # Fondo morado semi-transparente
                radius: [15, 15, 15, 15]
                padding: "15dp"
                elevation: 3
                
                MDLabel:
                    id: display
                    text: ""
                    font_style: "H3"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    halign: "right"

        # --- CUERPO (Teclado + Historial) ---
        MDBoxLayout:
            size_hint_y: 0.65
            spacing: "15dp"
            padding: ["20dp", "10dp", "20dp", "20dp"]

            # Teclado Numérico (Grid)
            MDGridLayout:
                cols: 5
                spacing: "8dp"
                size_hint_x: 0.6

                # Fila 1
                BotonCalc:
                    text: "7"
                    on_release: app.press("7")
                BotonCalc:
                    text: "8"
                    on_release: app.press("8")
                BotonCalc:
                    text: "9"
                    on_release: app.press("9")
                BotonCalc:
                    text: "C"
                    md_bg_color: 0.5, 0.1, 0.3, 0.85
                    on_release: app.press("C")
                BotonCalc:
                    text: "AC"
                    md_bg_color: 0.7, 0.2, 0.2, 0.85
                    on_release: app.press("AC")

                # Fila 2
                BotonCalc:
                    text: "4"
                    on_release: app.press("4")
                BotonCalc:
                    text: "5"
                    on_release: app.press("5")
                BotonCalc:
                    text: "6"
                    on_release: app.press("6")
                BotonCalc:
                    text: "+"
                    md_bg_color: 0.8, 0.2, 0.5, 0.85
                    on_release: app.press("+")
                BotonCalc:
                    text: "-"
                    md_bg_color: 0.8, 0.2, 0.5, 0.85
                    on_release: app.press("-")

                # Fila 3
                BotonCalc:
                    text: "1"
                    on_release: app.press("1")
                BotonCalc:
                    text: "2"
                    on_release: app.press("2")
                BotonCalc:
                    text: "3"
                    on_release: app.press("3")
                BotonCalc:
                    text: "*"
                    md_bg_color: 0.8, 0.2, 0.5, 0.85
                    on_release: app.press("*")
                BotonCalc:
                    text: "/"
                    md_bg_color: 0.8, 0.2, 0.5, 0.85
                    on_release: app.press("/")

                # Fila 4
                BotonCalc:
                    text: "0"
                    on_release: app.press("0")
                BotonCalc:
                    text: "."
                    on_release: app.press(".")
                BotonCalc:
                    text: "("
                    md_bg_color: 0.4, 0.2, 0.6, 0.85
                    on_release: app.press("(")
                BotonCalc:
                    text: ")"
                    md_bg_color: 0.4, 0.2, 0.6, 0.85
                    on_release: app.press(")")
                BotonCalc:
                    text: "="
                    md_bg_color: 1, 0.4, 0.7, 0.9 
                    on_release: app.press("=")

            # Panel de Historial
            MDCard:
                size_hint_x: 0.4
                md_bg_color: 0.2, 0.1, 0.35, 0.7  # Fondo morado semi-transparente
                radius: [15, 15, 15, 15]
                orientation: "vertical"
                padding: "10dp"
                elevation: 3

                MDLabel:
                    text: "HISTORIAL"
                    font_style: "Subtitle1"
                    theme_text_color: "Custom"
                    text_color: 1, 0.6, 0.8, 1
                    halign: "center"
                    size_hint_y: 0.15

                MDSeparator:
                    color: 1, 0.6, 0.8, 1

                ScrollView:
                    size_hint_y: 0.85
                    MDList:
                        id: history_list
'''

class KuromiCalcApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def press(self, button_text):
        current = self.root.ids.display.text

        if button_text == "AC":
            self.root.ids.display.text = ""
            
        elif button_text == "C":
            self.root.ids.display.text = current[:-1]
            
        elif button_text == "=":
            try:
                result = str(eval(current))
                self.root.ids.display.text = result
                
                history_item = f"{current} = {result}"
                nuevo_item = OneLineListItem(
                    text=history_item, 
                    theme_text_color="Custom", 
                    text_color=(0.9, 0.8, 1, 1)
                )
                self.root.ids.history_list.add_widget(nuevo_item)
                
            except Exception:
                self.root.ids.display.text = "Error"
                
        else:
            if current == "Error":
                self.root.ids.display.text = button_text
            else:
                self.root.ids.display.text = current + button_text

if __name__ == '__main__':
    KuromiCalcApp().run()