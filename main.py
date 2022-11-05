print("\n\n")

class Alumno:
  def __init__(self, nombre, nota):
    self.nombre= nombre
    self.nota= nota
    print("El alumno se ha creado con éxito\n")

  def datos(self):
    print("Nombre: ",self.nombre)
    print("Nota: ",self.nota)

  def califiacion(self):
    if self.nota>=5:
      print(self.nombre, "ha aprobado")
    else:
      print(self.nombre, "ha suspendido")


alumno1=Alumno("Jaime", 5)
alumno1.datos()
alumno1.califiacion()

print("\n\n")

alumno2=Alumno("Alejandro", 3)
alumno2.datos()
alumno2.califiacion()
  
  