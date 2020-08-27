"""Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

print('{:=^40}'.format(' LOLJA '))
p = float(input('Qual o valor das compras? R$'))
cond = int(input('[1] À vista dinheiro ou cheque'
             '\n[2] À vista no cartão'
             '\n[3] Até 2x no cartão'
             '\n[4] 3x ou mais no cartão'
             '\nQual será a forma de pagamento? '))
total = p
if cond == 1:
    total = p * 0.9
    print('Você terá 10% de desconto')
elif cond == 2:
    total = p * 0.95
    print('Você terá 5% de desconto')
elif cond == 3:
    total = p
elif cond == 4:
    total = p * 1.2
    print('{:*^40}'.format(' Nessa opção há 20% de juros '))
    np = int(input('Você quer parcelar em quantas vezes? '))
    if np > 12:
        print('O máximo nessa forma de pagamento é de 12 parcelas!!!')
        np = 12
    elif np < 3:
        print('O mínimo nessa forma de pagamento é de 3 parcelas!!!')
        np = 3
    print('Você pagará {} parcelas de R${:.2f}'.format(np, (p * 1.2) / np))
#else:
    #print('Escolha uma das quatro opções!!!')
print('O valor das compras ficará R${}'.format(total))
