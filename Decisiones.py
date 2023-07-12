import random

options = ['Piedra', 'Papel', 'Tijeras']
user_wins = 0
cpu_wins = 0
round = 1

while True:
    print('*' * 30)
    print('ROUND', round)
    print('*' * 30)

    print('Puntos - Tú:', user_wins)
    print('Puntos - CPU:', cpu_wins)

    user_option = input('Selecciona uno entre Piedra, Papel o Tijeras ')
    user_option = user_option.capitalize()

    cpu_option = random.choice(options)

    round += 1

    if not user_option in options:
        print('Parece que no es una opcion valida, intentalo de nuevo')
        continue

    if user_option == cpu_option:
        print('Es un Empate!')
    elif user_option == 'Tijeras':
        if cpu_option == 'Piedra':  
            print('Piedra gana a Tijeras, Jarvis gana!')
            cpu_wins += 1
        else:
            print('Tijeras gana a Papel, tu ganas!')
            user_wins += 1
    
    elif user_option == 'Piedra':
        if cpu_option == 'Tijeras':
            print('Piedra gana a Tijeras, tu ganas!')
            user_wins += 1
        else:
            print('Papel gana a Piedra, Jarvis gana!')
            cpu_wins += 1
    
    elif user_option == 'Papel':
        if cpu_option == 'Tijeras':
            print('Tijeras gana a Papel, Jarvis gana!')
            cpu_wins += 1
        else:
            print('Papel gana a Piedra, tu ganas!')
            user_wins += 1
    
    if cpu_wins == 2:
        print('Jarvis ha Ganado, gracias por participar!')
        break

    if user_wins == 2:
        print('Has ganado! esperamos vuelvas pronto!')
        break


        

    

    


    
