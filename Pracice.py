#Funcion para calcular el numero mayor.
def numero_mayor(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

print(numero_mayor(5,7))

#Funcion para calcular el numero mayor entre 3 opciones.
def numero_mayor_3(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
    
print(numero_mayor_3(6,2,5))

#Funcion para invertir palabras.
def palabra_invertida(cadena):
    cadena_invertida = ''
    for l in cadena:
        cadena_invertida = l + cadena_invertida
    return cadena_invertida

print(palabra_invertida('Holaaaa'))

#Funcion que cuenta la cantidad de letras en una cadena.
def word_counter(cadena):
    word = 'h'
    counter = 0
    for l in cadena:
        if l.lower() == word:
            counter += 1
    return counter

print(word_counter('HolaaaaaAaaaa'))

#Funcion que valora si una letra es vocal o no.
def is_vocal(n):
    vocal ='aeiouAEIOU'
    if n in vocal:
        return 'Esta es una vocal!'
    else:
        return 'Esta no es una vocal!'

print(is_vocal('a'))

#Funcion que calcula si un numero es par o impar.
def is_par(n):
    if n % 2 == 0:
        return 'Este numero es par!'
    else:
        return 'Este numero es impar!'

print(is_par(13))