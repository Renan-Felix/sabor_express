import os;

restaurantes = [{'nome' : 'Sushi house', 'departamento' : 'Japonesa', 'ativo': False}, {'nome': 'Pizza hot', 'departamento': 'Pizza', 'ativo': True},
 {'nome': 'Massarena', 'departamento': 'Italiana', 'ativo': True}]

def exibir_nome_do_programa():
    '''Exibe o nome do programa de forma estilizada'''
    print('''
█▀▀ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ ░░ █▀▀ █░█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
▀▀█ █▄▄█ █▀▀▄ █░░█ █▄▄▀ ▀▀ █▀▀ ▄▀▄ █░░█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ ░░ ▀▀▀ ▀░▀ █▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀▀▀
      
      ''');

def exibir_opcoes():
    '''Exibe as opções disponíveis no menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Exibe a mensagem Finalizando app, e logo depois encerra o programa'''
    exibir_subtitulos('Finalizando app...')

def voltar_menu_principal():
    '''Essa opção pede uma tecla para voltar ao menu principal
    Outputs:
    - Volta ao menu principal após selecionado a tecla
    
    '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Exibe a mensagem de opção inválida e retorna ao menu principal
    
    Outputs:
    - Retorna ao menu principal
    
    '''
    print('Opção inválida!\n')
    voltar_menu_principal()

def exibir_subtitulos(texto):
    '''Exibe um subtitulo estilizado na tela
    
    Inputs:
    - texto: str - O texto do subtitulo
    
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Departamento do restaurante

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulos('Cadastro de novos restaurantes')
    nome_do_resturante = input('Digite o nome do restaurante que deseja cadastrar: ')
    departamento_restaurante = input(f'Digite o departamento do restaurante {nome_do_resturante}: ')
    dados_restaurante ={'nome': nome_do_resturante, 'departamento': departamento_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante  {nome_do_resturante} foi cadastrado com sucesso!')
    voltar_menu_principal()


def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes disponíveis.
    
    Outputs:
    - Realiza a saída dos subtitulos de cada informação sobre o restaurante, exemplos:Nome do restaurante, categoria e status.
    - Realiza a saída dos dados contendo o nome do restaurante, qual departamento ele se encontra e se está ativo ou desativado.
    
    
    
    '''
    exibir_subtitulos('Listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(24)} | {'Categoria'.ljust(24)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        departamento = restaurante['departamento']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        
        print(f'- {nome_restaurante.ljust(24)} | {departamento.ljust(24)} | {ativo}')

    voltar_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é para fazer a mudança do status do restaurante, por exemplo ativar ou desativar o restaurante
    
    Inputs:
    - Pede o nome do restaurante que quer alterar o estado


    Outputs:
    - Exibe a mensagem indicando o sucesso da operação
    '''
    exibir_subtitulos('Alternando estado do restaurante')
    nome_restaurente = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurente == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurente} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurente} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')




    voltar_menu_principal()


def escolher_opcao():
    '''Solicita e executa a opção escolhida pelo usuário
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida);

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida ==3:
            alternar_estado_restaurante()
        elif opcao_escolhida ==4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()






