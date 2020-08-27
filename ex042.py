"""Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""

a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))
tipo = '\033[1:32mEquilátero!!!'
if a != b != c != a:
    tipo = '\033[1:32mEscaleno!!!'
elif a == b != c or b == c != a or a == c != b:
    tipo = '\033[1:32mIsósceles'
if abs(a - b) < c < (a + b) and abs(a - c) < b < (a + c) and abs(b - c) < a < (b + c):
    print('Os lados {}, {} e {} formam um triângulo {}'.format(a, b, c, tipo))
else:
    print('Os lado {}, {} e {} não formam um triângulo'.format(a, b, c))
