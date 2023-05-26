

# FUNCION 1 ORIGINAL

def contar_caracteres(cadena):
    letras = 0
    numeros = 0
    caracteres_especiales = 0
    
    for caracter in cadena:
        if caracter.isalpha():
            letras += 1
        elif caracter.isdigit():
            numeros += 1
        else:
            caracteres_especiales += 1
    
    print("Letras =", letras)
    print("Números =", numeros)
    print("Caracteres especiales =", caracteres_especiales)


cadena = input("Ingrese una cadena de texto: ")
contar_caracteres(cadena)

# Al ejecutar este código, se te solicitará ingresar una cadena de texto. 
# Luego, la función 'contar_caracteres_funcional' se llamará con la cadena ingresada y se imprimirá la cantidad de letras, números y caracteres especiales presentes en la cadena.
# La función lambda utiliza expresiones lambda, la función 'map()' y la función 'sum()' para contar los caracteres de diferentes categorías en la cadena de texto.
# Por ejemplo, si ingresamos la cadena "Hola 123#", el resultado del llamado de prueba sería:

# Ingrese una cadena de texto: Hola 123#
# Letras = 4
# Números = 3
# Caracteres especiales = 1

# Esto indica que hay 4 letras, 3 números y 1 carácter especial en la cadena ingresada.



# FUNCION 1 PROGRAMACION FUNCIONAL

contar_caracteres_funcional = lambda cadena: (
    print("Letras =", sum(map(lambda c: c.isalpha(), cadena))),
    print("Números =", sum(map(lambda c: c.isdigit(), cadena))),
    print("Caracteres especiales =", sum(map(lambda c: not c.isalnum(), cadena)))
)

cadena = input("Ingrese una cadena de texto: ")
contar_caracteres_funcional(cadena)

# Entrada: 
# Hola! 123 Mundo
# Salida: 
# Letras = 8
# Números = 3
# Caracteres especiales = 3

# Se ingresa la cadena "Hola! 123 Mundo" cuando se solicita la entrada. 
# La función 'contar_caracteres_funcional' se encarga de contar el número de letras, números y caracteres especiales en la cadena.
# La salida esperada muestra que hay 8 letras en la cadena ("H", "o", "l", "a", "M", "u", "n", "d"), 3 números ("1", "2", "3") y 3 caracteres especiales ("!", " ", " ").
# La función lambda utiliza expresiones lambda, la función 'map()' y la función 'sum()' para contar los caracteres de diferentes categorías en la cadena de texto.
# La función 'print()' se utiliza para imprimir los resultados en el formato "Etiqueta = Valor" para cada categoría.



# FUNCION 2 ORIGINAL

def contar_apariciones(cadena):
    apariciones = {}
    for caracter in cadena:
        if caracter in apariciones:
            apariciones[caracter] += 1
        else:
            apariciones[caracter] = 1
    print(apariciones)

cadena = input("Ingrese una cadena de texto, números o símbulos:")
contar_apariciones(cadena)

# Entrada:
# Hello, World!
# Salida:
# {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1}

# ingresamos la cadena "Hello, World!" cuando se solicita la entrada. 
# La función contar_apariciones se encarga de contar las apariciones de cada caracter en la cadena y almacenar los resultados en un diccionario.
# La salida esperada muestra el diccionario de apariciones, donde cada clave representa un caracter y el valor asociado representa la cantidad de veces que aparece en la cadena.
# En este ejemplo, el caracter "H" aparece una vez, "e" aparece una vez, "l" aparece tres veces, 
# "o" aparece dos veces, "," aparece una vez, " " (espacio) aparece una vez, "W" aparece una vez, 
# "r" aparece una vez, "d" aparece una vez y "!" aparece una vez.



# FUNCION 2 PROGRAMACION FUNCIONAL

contar_apariciones_funcional = lambda cadena: print(
    {caracter: sum(map(lambda c: c == caracter, cadena)) for caracter in set(cadena)}
)

cadena = input("Ingrese una cadena de texto, números o símbolos: ")
contar_apariciones_funcional(cadena)

# Entrada:
# Hello, World!
# Salida:
# {' ': 1, 'o': 2, ',': 1, 'H': 1, 'e': 1, 'r': 1, 'W': 1, '!': 1, 'l': 3, 'd': 1}

# Se ingresa la cadena "Hello, World!" cuando se pide la entrada. 
# La funcion 'contar_apariciones_funcional' se encarga de contar las apariciones de cada caracter en la cadena utilizando un enfoque funcional.
# La salida esperada muestra un diccionario donde cada clave representa un caracter presente en la cadena y el valor asociado representa la cantidad de veces que aparece.
# Aquí el caracter " " (espacio) aparece una vez, "o" aparece dos veces, "," aparece una vez, 
# "H" aparece una vez, "e" aparece una vez, "r" aparece una vez, "W" aparece una vez, "!" aparece una vez, 
# "l" aparece tres veces y "d" aparece una vez.



# FUNCION 3 ORIGINAL

def eliminar_elemento(lista, elemento):
    while elemento in lista:
        lista.remove(elemento)

mi_lista = [1, 2, 3, 4, 2, 5, 7, 10, 100, 589, 85]
eliminar_elemento(mi_lista, 85)
print(mi_lista)

# Se tiene una lista inicial 'mi_lista' con elementos [1, 2, 3, 4, 2, 5, 7, 10, 100, 589, 85]. 
# Se desea eliminar el elemento '85' de la lista utilizando la función 'eliminar_elemento'.
# La salida esperada será la lista modificada después de eliminar el elemento:
# [1, 2, 3, 4, 2, 5, 7, 10, 100, 589]
# Se utiliza una función lambda junto con la función 'filter()' para filtrar los elementos de la lista, 
# manteniendo solo aquellos que no sean igual al elemento que se va a eliminar.
# Se asigna el resultado de la función 'eliminar_elemento_funcional' a 'mi_lista' y luego se imprime la lista modificada.



# FUNCION 3 PROGRAMACION FUNCIONAL

eliminar_elemento_funcional = lambda lista, elemento: list(filter(lambda x: x != elemento, lista))

mi_lista = [1, 2, 3, 4, 2, 5, 7, 10, 100, 589, 85]
mi_lista = eliminar_elemento_funcional(mi_lista, 85)
print(mi_lista)

# Lista inicial 'mi_lista' con los siguientes números [1, 2, 3, 4, 2, 5, 7, 10, 100, 589, 85]. 
# Se desea eliminar el elemento '85' de la lista utilizando la función 'eliminar_elemento_funcional'.
# La salida esperada será la lista modificada después de eliminar el elemento:
# [1, 2, 3, 4, 2, 5, 7, 10, 100, 589]
# En el enfoque funcional, utilizamos una función lambda junto con la función 'filter()' para filtrar los elementos de la lista, teniendo solo los números que no se desean eliminar.
# El resultado de la función 'eliminar_elemento_funcional' irá a 'mi_lista' y luego imprimimos la lista modificada.



# FUNCION 4 ORIGINAL

def imprimir_lista_y_tupla(secuencia):
    lista = []
    for numero in secuencia:
        lista.append(int(numero))
    tupla = tuple(lista)
    print("Lista:", lista)
    print("Tupla:", tupla)

entrada = input("Ingrese una secuencia de números separados por comas: ")
numeros = entrada.split(",")
imprimir_lista_y_tupla(numeros)

# Se solicita al usuario que ingrese una X cantidad de números separados por comas. 
# Ejemplo, si el usuario ingresa "1,2,3,4,5", los números se convierten en una lista de cadenas numeros = ['1', '2', '3', '4', '5'].
# Luego se utiliza la función int() para convertir cada cadena de números en la lista original a un entero. 
# Se utiliza map(int, secuencia) para llevar la función int() a cada elemento de la secuencia.
# Finalmente, se imprime la lista y la tupla resultantes utilizando la función print().



# FUNCION 4 PROGRAMACION FUNCIONAL

imprimir_lista_y_tupla_funcional = lambda secuencia: (
    print("Lista:", list(map(int, secuencia))),
    print("Tupla:", tuple(map(int, secuencia)))
)

entrada = input("Ingrese una secuencia de números separados por comas: ")
numeros = entrada.split(",")
imprimir_lista_y_tupla_funcional(numeros)

# Supongamos que el usuario ingresa la secuencia "1,2,3,4,5". 
# El resultado esperado será:
# Lista: [1, 2, 3, 4, 5]
# Tupla: (1, 2, 3, 4, 5)

# Se utiliza una función lambda para definir 'imprimir_lista_y_tupla_funcional'. 
# Esta función toma una secuencia de números separados por comas y realiza lo siguiente:
# Utiliza 'map(int, secuencia)' para convertir cada elemento de la secuencia de cadenas a un entero.
# Luego, genera una lista con 'list(map(int, secuencia))' y la imprime utilizando 'print("Lista:", ...)'.
# Además, genera una tupla con 'tuple(map(int, secuencia))' y la imprime utilizando 'print("Tupla:", ...)'.