#print('Olá Mundo')
#print(2+3)
#print('2+3')
#print('2' + '3')
#print('O resultado de 2 + 3 e: ', 2 + 3)
#print(10*(5 + 7)/4)

#nota = 8.5
#disciplina = "Lógica de programação"
#print('Disciplina: ', disciplina, ' Nota: ', nota)


#idade = int(input('Digite a idade: '))
#print(idade)
#nome = input('Digite seu nome: ')
#print(f'Olá {nome}, seja bem vindo!')

#nota = float(input('Digite sua nota: '))
#if nota >= 7.0:
#    print('Parabéns você foi Aprovado!')
#else:
#    print(f'Você tirou nota {nota}, Reprovado!')

x = int(input('Digite o primeiro numero: '))
y = int(input('Digite o segundo numero: '))

# MANEIRA MODERNA
resultado = 'O resultado da soma de {} com {} é {}'.format(x, y, x + y)
print(resultado)

# MANEIRA COM f-string
resultado = f'O resultado da soma de {x} com {y} é {x + y}.'
print(resultado)

