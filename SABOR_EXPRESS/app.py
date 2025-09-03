import os

def exibir_nome_programa():
    print('\n 𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤 \n')

def exibir_opcoes():    
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair Restaurante')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app.\n')

def escolher_opcao():

    opcao_escolhida = int(input('Escolha uma das opções: '))
    if opcao_escolhida ==1:
        print('Cadastrar Restaurantes')
    elif opcao_escolhida ==2:
        print('Listar Restaurantes')    
    elif opcao_escolhida ==3:
        print('Ativar Restaurantes')    
    else:
        finalizar_app()

def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()