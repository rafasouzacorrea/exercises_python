"""Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida"""

peso = float(input('Peso(kg): '))
altura = float(input('Altura(m): '))
imc = peso / (altura**2)
print('Seu IMC é de {:.1f} \nVocê está numa condição de: '.format(imc), end='')
if imc < 18.5:
    print('\033[31mAbaixo do peso')
elif imc <= 25:
    print('\033[1:32mPeso ideal')
elif imc <= 30:
    print('\033[1:36mSobrepeso')
elif imc <= 40:
    print('\033[1:33mObesidade')
else:
    print('\033[1:31mObesidade mórbida')
