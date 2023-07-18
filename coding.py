
def calculator():
    operaciones = ('Suma', 'Resta', 'Multiplicacion', 'Division', 'Cerrar')
    opciones = (1, 2)
    

    while True:
        print('*' * 30)
        print('Bienvenido a Calculator')
        print('Presiona 1 para hacer calculos')
        print('Presiona 2 para salir')
        print('*' * 30)

        opcion_usuario = int(input('Ingresa tu opcion -> '))

        if not opcion_usuario in opciones:
            print(f'{opcion_usuario} no es una opcion valida, elige de nuevo')
            continue

        elif opcion_usuario == 2:
            print('Gracias por usar Calculator, esperamos vuelva pronto')
            break
        
        else:
             
            n1 = int(input('Ingresa el primer numero -> '))
            n2 = int(input('Ingresa el segundo numero -> '))
            operacion_usuario = input('Ingresa la operacion a realizar -> ')
            operacion_usuario = operacion_usuario.capitalize()

            if not operacion_usuario in operaciones:
                print(f'{operacion_usuario} no es una operacion valida, elige una entre: Suma, Resta, Multiplicacion o Division')
                continue

            if operacion_usuario == 'Suma':
                print(f'El resutaldo de tu {operacion_usuario} es')
                print(n1 + n2)
            
            elif operacion_usuario == 'Resta':
                print(f'El resutaldo de tu {operacion_usuario} es')
                print(n1 - n2)
            
            elif operacion_usuario == 'Multiplicacion':
                print(f'El resutaldo de tu {operacion_usuario} es')
                print(n1 * n2)
            
            else:
                print(f'El resutaldo de tu {operacion_usuario} es')
                print(n1 / n2)


       

if __name__ == '__main__':
    calculator()
