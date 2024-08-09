import random

numero_premiado = random.randint(0,10)
tentativas = 0

while True:
    palpite = int(input('Digite um valor de 0 a 10: '))

    if palpite != numero_premiado:
        tentativas +=1
        if palpite < 0 or palpite > 10:
            print('Escolha um número de 0 a 10!!!')
        elif palpite < numero_premiado:
            print('Muito baixo')
        elif palpite > numero_premiado:
            print('Muito alto')
    else:
        print(f'\nParabéns, você encontrou o número sorteado era: {numero_premiado}', 
              f'\nHouve {tentativas} para chegar no resultado')
        break

        
# print(numero_premiado)
