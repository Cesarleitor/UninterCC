km = int(input('Qual a quantidade de kms foram percorridos? '))
dias = int(input('Quantos dias foram percorridos? '))

preco = 60 * dias + 0.15 * km
print(f'Foi percorrido  {km} km em {dias} dias.')
print(f'Valor a ser pago: R${preco:.2f}')