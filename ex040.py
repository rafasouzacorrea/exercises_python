"""Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2
s = '\033[1:32mAprovado!!!\033[m'
c = '\033[1:32m'
f = '\033[m'
if m < 5:
    s = '\033[1:31mReprovado!!!\033[m'
    c = '\033[1:31m'
elif 7 > m >= 5:
    s = '\033[1:33mRecuperação!!!\033[m'
    c = '\033[1:33m'
print('Média: {}{}{} \nSua situação é: {}'.format(c, m, f, s))
