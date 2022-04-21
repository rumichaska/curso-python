# TIPOS DE DATOS ----------------------------------------------------------

# TEXTO

# Datos de tipo string o cadena de texto, se puede usar comillas simples o
# comillas dobles
palabra = "Esta es una variable de tipo string"

# NUMEROS

# Número enteros
entero = 28

# Número tipo float
decimal = 3.45

# Número complejos, se definen agregando una j
complejo = 1j

# Vamos a mostrar los resultados
print(palabra, entero, decimal, complejo)

# LISTAS

# Listas, colección de datos o varios datos agrupados
lista = []  # Lista vacía
print(lista)

# Lista con datos
lista_2 = [1, 2, 3]
print(lista_2)

# Copiar lista
lista_3 = lista_2.copy()

# Agregando valores a lista
lista_2.append(4)  # Método append

# Elimina los elementos de una lista
# lista_2.clear()
print(lista_2, lista_3)

# Para contar cuantas veces se repite un valor
print(lista_2, lista_2.count(2))  # Debemos indicar el valor a contar

# Para contar elementos de un objeto
print(len(lista_3), len(lista_2))  # Longitud, similar a length() de R

# Para acceder a elementos de una lista. Recordar que en python el primer
# elemento es 0
lista = ["hola", "diego", "32", "como", "estas", "guapo", 33]
print(lista[1])  # Similar a R pero contando desde 0

# Eliminando elementos de una lista
lista.pop()  # Elimina el último elemento de una lista
print(lista)

lista.remove("diego")  # Elimina un elemento en una posición
print(lista)

# Ordenar lista
lista.reverse()
print(lista)

lista.sort()  # El ordenamiento solo funciona con valores del mismo tipo
print(lista)

# TUPLAS
# Son parecidas a las listas pero su valores no se pueden modificar, tienen
# menos métodos que las listas, no se puede usar el método de append
tupla = ("Hola", "mundo", "somos", "tupla")
print(tupla)

# Contar elemento y ver la posición
print(tupla.count("tupla"), tupla.index("Hola"))

# Para modificar una tupla se debe convertir a una lista
listaTupla = list(tupla)
listaTupla.append("sol")
print(listaTupla)

# RANGOS
rango = range(8)
print(rango)

# DICCIONARIOS
