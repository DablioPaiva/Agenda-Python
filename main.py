def menu():
    voltar = 's'
    while voltar == 's':

        opcao = input('''
    ======================================================
                       Agenda Python
        
    MENU:
    [1]Adicionar Novo Contato
    [2]Listar Contato
    [3]Deletar Contato
    [4]Buscar Contato pelo Nome
    
    [0]Sair
        
    =======================================================
    Digite o número de uma das opções acima: ''')

        if opcao == '1':
            cadastrarContato()
        elif opcao == '2':
            listarContato()
        elif opcao == '3':
            deletarContato()
        elif opcao == '4':
            buscarContato()
        elif opcao == '0':
            sair()

        voltar = input(f'Deseja retornar ao MENU? (S/N) ').lower()

def cadastrarContato():
    idContato = input('Escolha o id do novo contato: ')
    try:
        if idContato == idContato:
            print(f'ID já existente. Digite outro ID.')
    except:
        return idContato
    nome = input('Digite o nome do novo contato: ')
    telefone = input('Digite o telefone do novo contato : ')
    try:
        agenda = open('agenda.txt', 'a')
        dados = f'{idContato}; {nome}; {telefone} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato adicionado com sucesso!')

    except:
        print('Erro ao adicionar o novo contato.')

    return print (f'O contato de ', nome, ' foi adicionado na lista de contatos.')


def listarContato():
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarContato():
    deletar = input(f'Digite o nome a ser deletado: ').lower()
    agenda = open('agenda.txt', 'r')
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if deletar not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open('agenda.txt', 'w')

    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso!')
    listarContato()


def buscarContato():
    busca = input(f'Digite o nome a ser buscado: ').lower()
    agenda = open('agenda.txt', 'r')

    for contato in agenda:
        if busca in contato.split(';')[1].lower():
            print(contato)
        else:
            print(f'O nome buscado não existe.')
    agenda.close()


def sair():
    print(f'Fechando aplicação . . .')
    exit()


def main():
    menu()
main()