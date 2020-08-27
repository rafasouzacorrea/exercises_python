"""Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
n = randint(0, 10)
c = 0
print('Vou pensar em um número entre 0 e 10... ')
print(n)
u = int(input('Tente adivinhar o número que eu pensei: '))
v = 'Mais'
while u != n:
    if u > 10 or u < 0:
        print('---É um número entre 0 e 10---')
    if u > n:
        v = 'Menos'
    c += 1
    u = int(input('{}!!!'
            '\nTente novamente: '.format(v)))
print('Acertou!!!!!'
      '\n{} foi o número que eu pensei e você precisou de {} palpites para adivinhar.'.format(n, c + 1))
