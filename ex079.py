"""Exercício Python 079: Crie um programa onde o usuário possa digitar
vários valores numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente. """

lista = []
a = 0
while True:
    a = int(input('Digite um valor qualquer ou 999 para sair: '))
    if a not in lista:
        lista.append(a)
    if lista[-1] == 999:
        lista.remove(999)
        break
lista.sort()
print(*lista, sep=', ')
