def calculator():
    opciones = (1, 2, 3, 4, 5)
    
    def suma(n1 , n2):
        resultsum = n1 + n2
        return resultsum

    def resta(n1, n2):
        resultres = n1 - n2
        return resultres

    def multiplicacion(n1, n2):
        resultmul = n1 * n2
        return resultmul

    def division(n1, n2):
        if n2 == 0:
            print("Error: No se puede dividir entre cero.")
            return None
        resultdiv = n1 / n2
        return resultdiv

    while True:
        
        print('*' * 30)
        print('Bienvenido a Calculator')
        print('*' * 30)  
        print('Menú:')
        print('Presiona 1 para Sumar')
        print('Presiona 2 para Restar')
        print('Presiona 3 para Multiplicar')
        print('Presiona 4 para Dividir')
        print('Presiona 5 para Salir')
        print('*' * 30)

        opcion_usuario = int(input('Ingresa tu opcion -> '))

        if not opcion_usuario in opciones:
            print(f'{opcion_usuario} no es una opcion valida, elige de nuevo')
            continue

        elif opcion_usuario == 5:
            print('Gracias por usar Calculator, esperamos vuelva pronto')
            break

        else:
             
            n1 = int(input('Ingresa el primer numero -> '))
            n2 = int(input('Ingresa el segundo numero -> '))

        if opcion_usuario == 1:
            result = suma(n1, n2)
            print(f'El resultado de tu suma es {result}!')
        
        elif opcion_usuario == 2:
            result = resta(n1, n2)
            print(f'El resultado de tu resta es {result}!')
        
        elif opcion_usuario == 3:
            result = multiplicacion(n1, n2)
            print(f'El resultado es de tu multiplicacion es {result}!')

        else:
            result = division(n1, n2)
            if result is not None:
                print(f'El resultado de tu division es {result}!')
            
            

if __name__ == '__main__':
    calculator()

