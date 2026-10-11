preco = float(input('Digite p preço do produto: '))
porcentagem = float(input('Digite a porcentagem de desconto (0-100%): '))

desconto = preco * (porcentagem / 100)
final = preco - desconto

print(f'O preço do produto é R${preco} Com o desconto de {porcentagem}%')
print(f'Valor calculado de desconto é R${desconto:.2f} Valor final 39do pruduto: R${final:.2f}')