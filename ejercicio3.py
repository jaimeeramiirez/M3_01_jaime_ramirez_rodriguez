print("\n\n")

class Producto:
  def __init__(self, codigo, nombre, precio, tipo):
    print("El producto se ha creado con éxito")
    self.codigo= codigo
    self.nombre= nombre
    self.precio= precio
    self.tipo = tipo

  def __str__(self):
        return """\
CODIGO\t{}
NOMBRE\t\t{}
PRECIO\t\t{}
TIPO\t{}""".format(self.codigo, self.nombre, self.precio, self.tipo)