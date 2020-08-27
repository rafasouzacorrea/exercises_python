"""Exercício Python 041: A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""

from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
cat = '\033[33mMIRIM'
if 9 < idade <= 14:
    cat = '\033[1:36mINFANTIL'
elif 14 < idade <= 19:
    cat = '\033[1:35mJÚNIOR'
elif 19 < idade <= 25:
    cat = '\033[1:31mSÊNIOR'
elif 25 < idade:
    cat = '\033[1:33mMASTER'
print('Ano: {} \nIdade: {} \nCategoria: {}'.format(ano, idade, cat))
