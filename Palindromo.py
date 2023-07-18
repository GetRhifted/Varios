def es_palindromo():
    frase = input('Ingresa una palabra o Frase ')
    frase = frase.lower()
    frase = frase.strip(' ')
    frase_invertida = ''
    for l in frase:
        frase_invertida = l + frase_invertida
    if frase_invertida == frase:
        return True
    else:
        return False
print(es_palindromo())

def es_primo():
    n = int(input('Ingresa un numero '))
    if n % n == 0 and n % 1 == 0:
        return True
    else:
        return False
    
print(es_primo())

def fibonacci():
    numero = int(input('Ingresa un numero '))
    if numero < 2:
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)
    
print(fibonacci())

####################################################################################

def es_palindromo(frase):
    frase = frase.lower().replace(' ', '')
    frase_invertida = frase[::-1]
    return frase == frase_invertida

frase = input('Ingresa una palabra o frase: ')
print(es_palindromo(frase))


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input('Ingresa un número: '))
print(es_primo(numero))


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

numero = int(input('Ingresa un número: '))
print(fibonacci(numero))
