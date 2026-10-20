def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while(x < min) or (x > max):
        x = int(input(pergunta))
    return x


def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!\n')


def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao criar o arquivo')
    else:
        a.write(f'{nomeJogo} - {nomeVideogame}\n')
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro na lista de arquivo')
    else:
        print(a.read())
    finally:
        a.close()



#PROGRAMA PRINCIPAL
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado com sucesso')
else:
    print('Arquivio inexistente')
    criarArquivo(arquivo)


while True:
    print('MENU')
    print('[1] Cadastrar um Item')
    print('[2] Listar todos os itens')
    print('[3] Sair')

    op = valida_int('Escolha a opcão desejada: ', 1, 3)
    if (op == 1): #NOVO ITEN
        print('Cadastrar novos itens selecionados..\n')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif (op == 2): #LISTAR
        print('Listar todos os itens selecionados..\n')
        listarArquivo(arquivo)

    elif (op == 3):
         print('Saindo do Programa')
         break

