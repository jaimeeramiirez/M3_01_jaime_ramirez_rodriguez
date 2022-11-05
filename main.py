#EJERCICIO 2

print("\n\n")
#EN UNA PRIMERA PARTE EL CÓDIGO ES IGUAL QUE EN EL EJERCICIO 1. Sin embargo, para este ejercicio utilizaremos el metodo __str__; este metodo nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto alumno1 creado y realizamos print(alumno1), Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).


class Alumno:
  def __init__(self, nombre, nota):
    self.nombre= nombre
    self.nota= nota
    print("El alumno se ha creado con éxito\n")
  
  def calificacion(self):
    if self.nota>=5:
      print(self.nombre, "ha aprobado")
    else:
      print(self.nombre, "ha suspendido")

  
  def __str__(self):
    return "{}, ha sacado un: {}".format(self.nombre, self.nota)

alumno1=Alumno("Jaime", 5)
print(alumno1)
calificacion= alumno1.calificacion()


