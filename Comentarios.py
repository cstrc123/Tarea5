
# FUNCION 1
contar_caracteres_funcional = lambda cadena: (
    print("Letras =", sum(map(lambda c: c.isalpha(), cadena))),
    print("Números =", sum(map(lambda c: c.isdigit(), cadena))),
    print("Caracteres especiales =", sum(map(lambda c: not c.isalnum(), cadena)))
)

cadena = input("Ingrese una cadena de texto: ")
contar_caracteres_funcional(cadena)

# Se utilizan expresiones lambda en combinación con las funciones 'map()' y 'sum()' para realizar las operaciones necesarias.
# La función 'map(lambda c: c.isalpha(), cadena)' se encarga de llevar cada caracter 'c' de la cadena 'cadena' a un valor que indica si es una letra.
# De igual manera 'map(lambda c: c.isdigit(), cadena)' lleva cada caracter 'c' a un valor que indica si es un número.
# Y 'map(lambda c: not c.isalnum(), cadena)' lleva cada caracter 'c' a un valor que indica si es un carácter especial.
# Luego se utiliza 'sum()' para obtener la suma de los valores, lo que nos da el conteo total de letras, números y caracteres especiales respectivamente.
# Finalmente, los resultados se imprimen directamente en la expresión 'lambda' utilizando la función 'print()'.


# FUNCION 2
contar_apariciones_funcional = lambda cadena: print(
    {caracter: sum(map(lambda c: c == caracter, cadena)) for caracter in set(cadena)}
)

cadena = input("Ingrese una cadena de texto, números o símbolos: ")
contar_apariciones_funcional(cadena)

# Se utiliza una expresión 'lambda' combinado con las funciones 'map()', 'sum()' y 'set()' para contar las apariciones de cada caracter en la cadena.
# Es importante la comprensión de diccionario '{caracter: sum(map(lambda c: c == caracter, cadena)) for caracter in set(cadena)}'.
# Aquí 'set(cadena)' crea un conjunto de caracteres únicos presentes en la cadena. 
# Luego para cada caracter en el conjunto, la expresión lambda 'lambda c: c == caracter' compara cada caracter 'c' de la cadena con el caracter actual del bucle.
# Devuelve 'True' si son iguales y 'False' en caso contrario. 
# Después, 'map()' aplica esta función lambda a cada caracter de la cadena.
# El resultado de 'map()' es una secuencia de valores que indican si cada caracter es igual al caracter actual del bucle. 
# Utilizamos 'sum()' para sumar estos valores, obteniendo así el número de apariciones del caracter en la cadena.
# Finalmente, el resultado se imprime en un diccionario utilizando 'print()'.


# FUNCION 3
eliminar_elemento_funcional = lambda lista, elemento: list(filter(lambda x: x != elemento, lista))

mi_lista = [1, 2, 3, 4, 2, 5, 7, 10, 100, 589, 85]
mi_lista = eliminar_elemento_funcional(mi_lista, 85)
print(mi_lista)

# Se usa una expresión lambda combinada con la función 'filter()' para eliminar el elemento deseado de la lista.
# La expresión lambda 'lambda x: x != elemento' se le pone a cada elemento 'x' de la lista. 
# Retorna 'True' si el elemento 'x' no es igual al elemento que queremos eliminar, y 'False' en un caso contrario. 
# Utilizando 'filter()', se filtran los elementos de la lista original, manteniendo solo los que cumplen con la expresión lambda.
# Finalmente, convertimos el resultado de 'filter()' en una lista utilizando 'list()', y el resultado de vuelta a 'mi_lista'.


# FUNCION 4
imprimir_lista_y_tupla_funcional = lambda secuencia: (
    print("Lista:", list(map(int, secuencia))),
    print("Tupla:", tuple(map(int, secuencia)))
)

entrada = input("Ingrese una secuencia de números separados por comas: ")
numeros = entrada.split(",")
imprimir_lista_y_tupla_funcional(numeros)

# Se utilizan expresiones lambda en combinación con las funciones 'map()' y 'print()' para transformar la secuencia de números y mostrar la lista y la tupla que corresponden.
# La expresión 'map(int, secuencia)' se encarga de aplicar la función 'int()' a cada elemento de la secuencia, convierte cada número de cadena a entero. 
# Se utiliza 'map()' una para crear la lista y otra para crear la tupla.
# Luego va la función 'print()' para mostrar la lista y la tupla como resultado.
# Se usa la sintaxis de tupla '(expresion1, expresion2)' para agrupar las dos llamadas a 'print()'.
