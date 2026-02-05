#importaciones

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.config import Config
from kivy.properties import NumericProperty
from kivy.properties import StringProperty

#llamar el documento kv
Builder.load_file("interface.kv")

#definir el tamano inicial de la calculadora
Config.set ('graphics', 'width', 520)
Config.set ('graphics', 'height', 850)


#variables a usar durante el transcurso de la codificacion
contador = NumericProperty(0)


#clase que contendra la interfaz y la logica

class Contenedor(BoxLayout):
    
    #en las funciones se hara lo siguiente:

    '''
    Se hara una funcion especificamente para agregar los numeros en pantalla
    esa funcion sera para los botones del 0-9

    y otra funcion para los parametros especiales (+-*/), donde se hara una condicion
    y dependiendo cual fue presionada se agregara a la cuenta
    '''

    #funcion para agregar los numeros

    def agregar_caracter(self, numero):

        #condicional para que no se acumulen los 0
        if self.ids.pantalla.text == "0":

            #condicional para que no sea agregado los operadores cuando se inicie el programa
            if numero == "+" or numero == "-" or numero == "*" or numero == "/" or numero == ".":
                self.ids.pantalla.text = "0"    

            else:
                self.ids.pantalla.text = numero
        
        else:
            self.ids.pantalla.text += numero 
        
        #boton para eliminar un caracter


    #funcion para calcular el total
    def calcular(self):
        
        variable = self.ids.pantalla.text
        total = eval(variable)
        self.ids.pantalla.text = str(total)



    #funcion para limpiar la pantalla
    def limpiar(self):
        self.ids.pantalla.text = "0"

    #funcion para eliminar un caracter de la pantalla

    def quitar_caracter(self):
        
        #tomar el texto actual y eliminarle un caracter
        variable = self.ids.pantalla.text
        variable2 = variable[:-1]

        if variable2 != "":
            self.ids.pantalla.text = variable2


#clase que llamara al proyecto

class MainApp(App):

    title = "Calculadora LuisMSB"

    def build(self):
        return Contenedor()
    
if __name__ == "__main__":
    MainApp().run()
