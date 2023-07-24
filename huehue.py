def invert_word():
    cadena = input('Ingresa una palabra o frase ')
    reversed_word = ''
    for l in cadena:
        reversed_word = l + reversed_word
    print(reversed_word) 


def vocals_only():
    cadena = input('Ingresa una frase o palabra ')
    vocals = 'AEIOaeiou'
    vocalscadena = []
    for l in cadena:
        if l in vocals:
            vocalscadena.append(l)
    print(f'Tu frase contiene las siguientes vocales {vocalscadena}')

vocals_only()