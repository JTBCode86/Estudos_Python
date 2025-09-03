import os
restaurantes =['Pizza','Sushi']

def exibir_nome_programa():
    print('\n 𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤 \n')

def exibir_opcoes():    
    print('1. Cadastrar Restaurantes')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurantes')
    print('4. Sair Restaurantes\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app...')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal\n')
    main()

def opcao_invalida():
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
  
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
  
    print(f'\n O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Listando os restaurantes')

    #lista de repetição utilização do for
    for restaurante in restaurantes:
        print(f'.{restaurante}') 

    voltar_ao_menu_principal()

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

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()