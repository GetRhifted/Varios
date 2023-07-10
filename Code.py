def numero_par():
    n = int(input('Dime un numero! '))
    if n % 2 == 0:
        return 'Este es un numero par!'
    else:
        return 'Este es un numero impar, imbecil...'

print(numero_par())

def reversed_word():
    cadena = input('Ingresa una palabra! ')
    cadena_invertida = ''
    for l in cadena:
        cadena_invertida = l + cadena_invertida
    return cadena_invertida

print(reversed_word())