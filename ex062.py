"""Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se
ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que
quer mostrar 0 termos."""
a1 = float(input('Primeiro termo: '))
r = float(input('Razão: '))
n = 1
v = ''
p = 's'
an = 0
while n < 11:
    an = a1 + r * (n - 1)
    n += 1
    if an.is_integer() is True:
        v += '{:.0f}'.format(an) + ' '
    else:
        v += '{:.2f}'.format(an) + ' '
print(v)
while 's' in p:
    p = str(input('\nVocê deseja mostrar mais números? [sim] [não]: ')).lower().strip()
    if p == 'sim' or p == 'nao' or p == 'não':
        if p[0] == 'n':
            print('Primeiro termo dessa PA: a1 = {} \nÚltimo termo: a{} = {}'.format(a1, n - 1, an))
            print('FIM')
        elif p[0] == 's':
            qnt = int(input('Quantos? '))
            for c in range(0, qnt):
                an = a1 + r * (n - 1)
                n += 1
                if an.is_integer() is True:
                    v += '{:.0f}'.format(an) + ' '
                else:
                    v += '{:.2f}'.format(an) + ' '
            print(v)
    else:
        p = 's'
        print('Resposta inválida')
