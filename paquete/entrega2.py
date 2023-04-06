
from modulos.entrega1 import *

class Cliente():
      especie="Persona Física"
  caracteristica="Atleta" 


  def __init__(self, nombre, edad, ciudad, deporte): 
    self.nombre = nombre
    self.edad = edad
    self.ciudad = ciudad
    self.deporte = deporte  
        

  def registro(self):
    print("Hola! Te registraste con éxito!!! ")

  def armar carrito(self):
    print("Producto añadido")

  def comprar(self):
    print("Estoy finalizando mi compra")

  
  def __str__(self): #metodo especial
    return(f"hola soy {self.nombre} y soy amante de este deporte:{self.deporte}")


