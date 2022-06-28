from func import*

class Menu:
   def __init__(self):
    Funço = funço()
        
        
    while True:
        entrada = input('1 - Salvar Produtos\n2 - Listar Produtos\n3 - Buscar produto\n4 - Alterar Produto\n0 - Sair')
        if entrada == '1':
            funço.salvar_produtos()

        elif entrada == '2':
            funço.listar_produtos()

        elif entrada == '3':
            funço.buscar_produto()

        elif entrada == '4':
            funço.alterar_produto()
         
        elif entrada == '0':
            break
        else:
            print('erro')



