import os

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
            print('\n -> Cadastrar Restaurantes <-\n')
        elif opcao_escolhida ==2:
            print('\n -> Listar Restaurantes <-\n')    
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

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()