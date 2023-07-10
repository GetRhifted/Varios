import random

def main():
    limite_minimo = int(input('Ingresa el numero mas bajo del rango '))
    limite_maximo = int(input('Ingresa el numero mas alto del rango '))
    numero_secreto = random.randint(limite_minimo, limite_maximo)
    intentos = 0

    while True:
        intentos += 1
        numero_usuario = int(input('Ingresa el numero que intentas adivinar! '))
        if numero_usuario < numero_secreto:
            print('Intenta un numero mas grande!')
        elif numero_usuario > numero_secreto:
            print('Intenta un numero mas pequeño!')
        else:
            print(f'Felicitaciones! has adivinado el numero! Te ha tomado {intentos} intentos!')
            break

if __name__ == '__main__':
     main()