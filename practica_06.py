# OBJETOS CLASES Y HERENCIAS ----------------------------------------------

# Clases
class Usuario:
    # Propiedades de la clase
    nombre = "Diego"
    apellido = "Castro"

usuario = Usuario()
usuario2 = Usuario()

print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

# Para crear una clase con varias propiedades
class Mascota:
    # definiendo método __init__, 'self' hace una referencia a sí mismo
    def __init__(self, nombre, dueño):
        self.nombre = nombre
        self.dueño = dueño

mascota = Mascota("Danton", "Diego")
mascota2 = Mascota("Valentina", "Gladys")

print(mascota.nombre, mascota.dueño)
print(mascota2.nombre, mascota2.dueño)

# Método para crear un saludo con la información del nombre y apellido
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def saludo(self):
        print("Hola! mi nombre es", self.nombre, self.apellido)
# Para definir las propiedades del usuario
usuario = Usuario("Diego", "Castro")
usuario2 = Usuario("Carmen", "Pérez")
# Para llamar el método saludo
usuario.saludo()
usuario2.saludo()
