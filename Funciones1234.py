

# FUNCIONES CON PROGRAMACIÓN FUNCIONAL

# FUNCION 1
contar_caracteres_funcional = lambda cadena: (
    print("Letras =", sum(map(lambda c: c.isalpha(), cadena))),
    print("Números =", sum(map(lambda c: c.isdigit(), cadena))),
    print("Caracteres especiales =", sum(map(lambda c: not c.isalnum(), cadena)))
)

cadena = input("Ingrese una cadena de texto: ")
contar_caracteres_funcional(cadena)



# FUNCION 2
contar_apariciones_funcional = lambda cadena: print(
    {caracter: sum(map(lambda c: c == caracter, cadena)) for caracter in set(cadena)}
)

cadena = input("Ingrese una cadena de texto, números o símbolos: ")
contar_apariciones_funcional(cadena)



# FUNCION 3
eliminar_elemento_funcional = lambda lista, elemento: list(filter(lambda x: x != elemento, lista))

mi_lista = [1, 2, 3, 4, 2, 5, 7, 10, 100, 589, 85]
mi_lista = eliminar_elemento_funcional(mi_lista, 85)
print(mi_lista)



# FUNCION 4
imprimir_lista_y_tupla_funcional = lambda secuencia: (
    print("Lista:", list(map(int, secuencia))),
    print("Tupla:", tuple(map(int, secuencia)))
)

entrada = input("Ingrese una secuencia de números separados por comas: ")
numeros = entrada.split(",")
imprimir_lista_y_tupla_funcional(numeros)
