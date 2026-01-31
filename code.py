'''
Codigo de LuisMSB 
'''


import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.config import Config
from kivy.properties import StringProperty, ObjectProperty  #libreria para el manejo de los buttons
from kivy.properties import NumericProperty

#Agregar un tamaño adaptado para celulares, si se abre en computadora, este tendra un limite
Config.set ('graphics', 'width', 720)
Config.set ('graphics', 'height', 1080)


#encargado de llamar al archivo kv
Builder.load_file ('interface.kv')



#clase que contiene la interfaz y logica del proyecto

class Contenedor (GridLayout):
    
    #funciones logicos
    
    contador = NumericProperty(0)   #contador, para tener un control del 0
    variable1 = NumericProperty(0)  #primera variable que se obtendra
    variable2 = NumericProperty(0)  #segunda variable que se obtendra
    operacion = StringProperty("")
    punto_cant = NumericProperty(0)

    #funciones numericas

    def tecla_0(self):
        
        #condicional para no agregar un 0 sobre el 0

        if self.contador > 0:
        
            self.ids.pantalla.text += "0"
            self.contador += 1

    def tecla_1(self):

        if self.contador == 0:
            self.ids.pantalla.text = "1"
            self.contador += 1

        else:
            self.ids.pantalla.text += "1"
            self.contador += 1

    def tecla_2(self):

        if self.contador == 0:
            self.ids.pantalla.text = "2"
            self.contador += 1

        else:
            self.ids.pantalla.text += "2"
            self.contador += 1


    def tecla_3(self):

        if self.contador == 0:
            self.ids.pantalla.text = "3"
            self.contador += 1

        else:
            self.ids.pantalla.text += "3"
            self.contador += 1


    def tecla_4(self):
        
        if self.contador == 0:
            self.ids.pantalla.text = "4"
            self.contador += 1

        else:
            self.ids.pantalla.text += "4"
            self.contador += 1

    def tecla_5(self):
        
        if self.contador == 0:
            self.ids.pantalla.text = "5"
            self.contador += 1

        else:
            self.ids.pantalla.text += "5"
            self.contador += 1


    def tecla_6(self):

        if self.contador == 0:
            self.ids.pantalla.text = "6"
            self.contador += 1

        else:
            self.ids.pantalla.text += "6"
            self.contador += 1


    def tecla_7(self):


        if self.contador == 0:
            self.ids.pantalla.text = "7"
            self.contador += 1

        else:
            self.ids.pantalla.text += "7"
            self.contador += 1

    def tecla_8(self):

        
        if self.contador == 0:
            self.ids.pantalla.text = "8"
            self.contador += 1

        else:
            self.ids.pantalla.text += "8"
            self.contador += 1


    def tecla_9(self):
        
        if self.contador == 0:
            self.ids.pantalla.text = "9"
            self.contador += 1

        else:
            self.ids.pantalla.text += "9"
            self.contador += 1


    #funciones de calculo

    def tecla_suma(self):
        self.contador = 0
        self.variable1 = self.ids.pantalla.text
        self.ids.pantalla.text = "0"
        self.operacion = "+"
        self.punto_cant = 0

        #intento de hacer cuentas progresivas


    def tecla_resta(self):
        self.contador = 0
        self.variable1 = self.ids.pantalla.text
        self.ids.pantalla.text = "0"
        self.operacion = "-"
        self.punto_cant = 0

    def tecla_multiplicar(self):
        self.contador = 0
        self.variable1 = self.ids.pantalla.text
        self.ids.pantalla.text = "0"
        self.operacion = "*"
        self.punto_cant = 0

    def tecla_dividir(self):
        self.contador = 0
        self.variable1 = self.ids.pantalla.text 
        self.ids.pantalla.text = "0"
        self.operacion = "/"
        self.punto_cant = 0

    def tecla_punto(self):
        
        if self.punto_cant == 0:

            if self.contador > 0:
                self.ids.pantalla.text += "."
                self.punto_cant = 1



    def tecla_reset(self):

        #resetear todas las variables

        self.ids.pantalla.text = "0"
        self.contador = 0
        self.variable1 = 0  
        self.variable2 = 0 
        self.operacion = ""
        self.punto_cant = 0




    def tecla_enter(self):
        
        '''
        
            Primero se toma las 2 variables que contiene los operadores, siendo variable1 y variable2
            luego se suman y se pasan a una variable
            luego esa variable pasa a ser de tipo texto y se envia a la pantalla

        '''

        #reiniciar algunas variables
        self.punto_cant = 0

        #realizar operacion

        #condicional para detectar que operacion presiono el usuario
        if self.operacion == "+": 

            self.variable2 = self.ids.pantalla.text
            total = self.variable1 + self.variable2
            total_texto = str(total)
            texto_mostrar = ""

            x = 0
            y = 0
            #bucle while para buscar el caracter que tenga punto
            while y == 0:
                
                if total_texto[x] == ".":
                    print ("encontrado")
                    texto_mostrar += total_texto[x]
                    texto_mostrar += total_texto[x+1]
                    y = 1

                else:
                    print (total_texto[x])
                    texto_mostrar += total_texto[x]
                    x += 1
                

            self.ids.pantalla.text = texto_mostrar  
            
            
        
        if self.operacion == "-":

            self.variable2 = self.ids.pantalla.text
            total = self.variable1 - self.variable2
            total_texto = str(total)
            texto_mostrar = ""

            x = 0
            y = 0
            #bucle while para buscar el caracter que tenga punto
            while y == 0:
                
                if total_texto[x] == ".":
                    print ("encontrado")
                    texto_mostrar += total_texto[x]
                    texto_mostrar += total_texto[x+1]
                    y = 1

                else:
                    print (total_texto[x])
                    texto_mostrar += total_texto[x]
                    x += 1
                

            self.ids.pantalla.text = texto_mostrar  



        if self.operacion == "/":
                        
            self.variable2 = self.ids.pantalla.text
            total = self.variable1 / self.variable2
            total_texto = str(total)  
            texto_mostrar = ""

            x = 0
            y = 0
            #bucle while para buscar el caracter que tenga punto
            while y == 0:
                
                if total_texto[x] == ".":
                    print ("encontrado")
                    texto_mostrar += total_texto[x]
                    texto_mostrar += total_texto[x+1]
                    y = 1

                else:
                    print (total_texto[x])
                    texto_mostrar += total_texto[x]
                    x += 1
                

            self.ids.pantalla.text = texto_mostrar  


        if self.operacion == "*":
            
            self.variable2 = self.ids.pantalla.text
            total = self.variable1 * self.variable2
            total_texto = str(total)
            texto_mostrar = ""

            x = 0
            y = 0
            #bucle while para buscar el caracter que tenga punto
            while y == 0:
                
                if total_texto[x] == ".":
                    texto_mostrar += total_texto[x]
                    texto_mostrar += total_texto[x+1]
                    y = 1

                else:
                    print (total_texto[x])
                    texto_mostrar += total_texto[x]
                    x += 1
                

            self.ids.pantalla.text = texto_mostrar          


#clase que llama al proyecto

class MainApp(App):

    title ="calculadora LuisMSB"


    #ejecutar la interfaz
    def build(self):
        return Contenedor()


#ejecutador del proyecto

if __name__ == '__main__':
    MainApp().run()
