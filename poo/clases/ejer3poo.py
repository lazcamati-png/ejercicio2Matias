import math
class Ejercicio3():
    def __init__(self):
        while True:
            self.palabra = input("Palabra:")
            if self.palabra == "salir":
                break
            else:
                print(self.palabra)