#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
lista = ('pedra', 'papel', 'tesoura')
escolha = int(input('[0]Pedra '
                '\n[1]Papel '
                '\n[2]Tesoura '
                '\nEscolha uma das opções: '))
pc = int(randint(0, 2))
print('Pedra...')
sleep(1)
print('Papel...')
sleep(1)
print('Tesoura!!!')
sleep(0.5)
if escolha == 0 or escolha == 1 or escolha == 2:
    print('Você jogou {} e o Computador jogou {}'.format(lista[escolha], lista[pc]))
else:
    print('Valor inválido!')
if escolha == pc:
    print('EMPATE')
elif escolha == 0 and pc == 1 or escolha == 1 and pc == 2 or escolha == 2 and pc == 0:
    print('VOCÊ PERDEU!!!')
elif escolha == 0 and pc == 2 or escolha == 1 and pc == 0 or escolha == 2 and pc == 1:
    print('VOCÊ GANHOU!!!')

