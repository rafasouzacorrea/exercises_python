"""Exercício Python 053: Crie um programa que leia uma frase qualquer e diga
se ela é um palíndromo, desconsiderando os espaços."""

frase = str(input('Palavra: '))
lista = frase.lower().strip().split()
junta = ''.join(lista)
invertida = ''
print(junta)
for c in range(len(junta) - 1, -1, -1):
    invertida += junta[c]
if invertida == junta:
    print('{} é um palíndromo, pois {} de trás para frente é: {}'.format(frase, junta, invertida))
else:
    print('{} não é um palíndromo'.format(frase))
