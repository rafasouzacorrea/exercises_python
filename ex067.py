"""Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo. """

while True:
    print('-------------------')
    n = int(input('Número: '))
    if n < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{n}x{c} = {n * c}')
print('FIM')