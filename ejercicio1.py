#EJERCICIO 1 

print("\n\n")
#VAMOS A CREAR UNA CLASE LLAMADA ALUMNO, CON SU CONSTRUCTOR Y SUS ATRIBUTOS NOMBRE Y NOTA. CUANDO SE HAYA CREADO LA CLASE INDICAREMOS QUE SE HA CREADO CON ÉXITO Y POSTERIORMENTE CREAREMOS EL MÉTODO CALIFIACIÓN PARA PODER SABER SI EL ALUMNO HA APROBADO O SUSPENDIDO. 

class Alumno:
  def __init__(self, nombre, nota):
    self.nombre= nombre
    self.nota= nota
    print("El alumno se ha creado con éxito\n")
    print("Nombre: ", self.nombre)
    print("Nota: ", self.nota)
  
  def califiacion(self):
    if self.nota>=5:
      print(self.nombre, "ha aprobado")
    else:
      print(self.nombre, "ha suspendido")



alumno1=Alumno("Jaime", 5)
alumno1.califiacion()

print("\n\n")
  