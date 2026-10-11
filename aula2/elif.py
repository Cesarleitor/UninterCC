print('Escolha o item que deseja comprar:')
print('1 - Maçâ')
print('2 - Laranja')
print('3 - Banana')

prod = int(input('Informe o produto: '))
qtd = int(input('Informe a quantidade: '))

if prod == 1:
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} unidades de maçâs. Total a pagar: R${pagar:.2f}')
elif prod == 2:
    pagar = qtd * 3.6
    print(f'Você comprou {qtd} unidades de laranjas. Total a pagar: R${pagar:.2f}')
elif prod == 3:
    pagar = qtd * 1.85
    print(f'Você comprou {qtd} unidades de bananas. Total a pagar: R${pagar:.2f}')
else:
    print('Produto invalido')

