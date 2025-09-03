import os
restaurantes =['Pizza','Sushi']

def exibir_nome_programa():
    print('\n 𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤 \n')

def exibir_opcoes():    
    print('1. Cadastrar Restaurantes')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurantes')
    print('4. Sair Restaurantes\n')
    
def opcao_invalida():
    print('Opção invalida!\n')
    input('Digite uma tecla para voltar ao menu principal.\n')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma das opções: '))
        if opcao_escolhida ==1:
            #print('\n -> Cadastrar Restaurantes <-\n')
            cadastrar_novo_restaurante()
        elif opcao_escolhida ==2:
            listar_restaurante()
        elif opcao_escolhida ==3:
            print('\n -> Ativar Restaurantes <-\n')  
        elif opcao_escolhida ==4:
            finalizar_app()  
        else:
            opcao_invalida()
    except: 
            opcao_invalida()

def finalizar_app():
    os.system('cls')
    print('Finalizando o app...\n')

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
  
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
  
    print(f'\n O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    input('Digite uma tecla para voltar ao menu principal\n')
    main()

def listar_restaurante():
    os.system('cls')
    print('Listando os restaurantes\n')

    #lista de repetição utilização do for
    for restaurante in restaurantes:
        print(f'.{restaurante}') 

    input('Digite uma tecla para voltar ao menu principal\n')
    main()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()