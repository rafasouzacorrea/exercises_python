"""Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida
com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo
teclado (entre 0 e 20) e mostrá-lo por extenso."""

ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
       'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    print('-------------------------------------')
    n = int(input('Número entre 0 e 20: '))
    if n < 0 or n > 20:
        print('Valor inválido')
    else:
        print(f'{n} por extenso é: {ext[n]}')
        while True:
            r = input('Quer continuar? [s/n] ').lower().strip()
            if r == 's' or r == 'n':
                break
        if r == 'n':
            break
print('---------------fim--------------------')
