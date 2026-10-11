nome = input('Qual o seu nome?')
idade = int(input('Qual a sua idade?'))

if nome == 'Augusto':
    print('Olá Augusto que bom ter você sempre aqui!')
elif idade < 18:
    print('Você não e Augusto, e è menor de idade')
elif idade > 100:
    print('Diferente de você o Augusto não e Imortal!')
else:
    print(f'Olá {nome} seja bem vindo ao seu novo acesso! ')