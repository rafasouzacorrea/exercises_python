"""xercício Python 050: Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."""
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        cont += 1
        soma += n
print('A soma entre os {} números pares digitados é: {}'.format(cont, soma))
