'''
Codigo de LuisMSB 
'''


import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.config import Config

#Agregar un tamaño adaptado para celulares, si se abre en computadora, este tendra un limite

Config.set ('graphics', 'width', 720)
Config.set ('graphics', 'height', 1080)

class Contenedor (GridLayout):
    None

Builder.load_file ('interface.kv')

class MainApp(App):

    title ="calculadora LuisMSB"

    def build(self):
        return Contenedor()

if __name__ == '__main__':
    MainApp().run()
