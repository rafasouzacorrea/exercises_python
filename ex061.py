"""Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while."""

n = 1
a1 = float(input('Primeiro termo: '))
r = float(input('Razão: '))
t = False
print('Os dez primeiros termos de uma PA de primeiro termo {} e razão {} são:'.format(a1, r))
while n <= 10:
    an = a1 + r * (n - 1)
    t = an.is_integer()
    if t is True:
        if n == 10:
           print('{:.0f}'.format(an))
        else:
            print('{:.0f}'.format(an), end=', ')
    else:
        if n == 10:
            print('{:.2f}'.format(an))
        else:
            print('{:.2f}'.format(an), end=', ')
    n += 1
