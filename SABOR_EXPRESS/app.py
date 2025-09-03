import os

print('\n Sabor Express \n')

print('1. Cadastrar Restaurante')
print('2. Listar Restaurante')
print('3. Ativar Restaurante')
print('4. Sair Restaurante')

#opcao_escolhida = input('Escolha uma das opções: ')
opcao_escolhida = int(input('Escolha uma das opções: '))

def finalizar_app():
    os.system('cls')
    print('Finalizando o app.\n')
    
#print(f'Você escolheu a opção { opcao_escolhida}')
#print(opcao_escolhida == 1)
#print(type(opcao_escolhida))
#print(type(1))
#opcao_escolhida= int(opcao_escolhida)

if opcao_escolhida ==1:
    print('Cadastrar Restaurantes')
elif opcao_escolhida ==2:
    print('Listar Restaurantes')    
elif opcao_escolhida ==3:
    print('Ativar Restaurantes')    
else:
    #Implementar uma função no lugar do print. 
    #print('Encerrando o programa.')
    finalizar_app()