#CONDICIONAL COMPOSTA

print(' Escolha a fruta que deseja comprar!')
print('1 - Maçâ ')
print('2 - Laranja ')
print('3 - Banana')

produto = int(input('Digite o código do produto: '))
qtd = int(input('Digite a quantidade de itens: '))

# ESCOLHA MACÂ
if (produto == 1):
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} de maçâ. Total à pagar: R$ {pagar:.2f}')

# ESOLHA LARANJA
else:
    if produto == 2:
        pagar = qtd * 3.6
        print(f'Você comprou {qtd} de Laranjas. Total pagar:R$ {pagar:.2f}')

#ESOLHA BANANA
    else:
        if produto == 3:
            pagar = qtd * 1.85
            print(f'Você comprou {qtd} de Bananas. Total pagar: R$ {pagar:.2f}')

# ESCOLHA ERRADA
        else:
            print('Produdo inexistente!')
