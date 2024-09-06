# Lista inicial de nombres
nombres = [
    'Harry Houdini',
    'Newton',
    'David Blaine',
    'Hawking',
    'Messi',
    'Teller',
    'Einstein',
    'Pele',
    'Juanes'
]

# Grupos
magos = ['Harry Houdini', 'David Blaine', 'Teller']
cientificos = ['Newton', 'Hawking', 'Einstein']
otros = ['Messi', 'Pele', 'Juanes']

def hacer_grandioso():
    global magos
    magos = [f'El gran {magos[i]}' for i in range(len(magos))]

def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)


print("Lista completa de nombres antes de ser modificados:")
imprimir_nombres(nombres)

hacer_grandioso()

print("\nNombres de los magos grandiosos:")
imprimir_nombres(magos)

print("\nNombres de los científicos:")
imprimir_nombres(cientificos)

print("\nNombres de los otros:")
imprimir_nombres(otros)
