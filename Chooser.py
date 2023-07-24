import random

def chooser():
    opciones_input = input('Ingresa tus opciones separadas por una coma! ')
    opciones = opciones_input.split(',')
    seleccion = random.choice(opciones)
    print(f'La opcion seleccionada es {seleccion}!')


if __name__ == '__main__':
    chooser()