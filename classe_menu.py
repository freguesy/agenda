from pyparsing import Opt
from func import*

class Menu:
   def __init__(self):
    opt = Opt()
        
        
    while True:
        entrada = input('1 - Cadastro\n2 - Listar Produtos\n3 - Buscar produto\n4 - Alterar Produto\n0 - Sair')
        if entrada == '1':
            opt.salvar_produtos()

        elif entrada == '2':
            opt.listar_produtos()

        elif entrada == '3':
            opt.listar_produtos()

        elif entrada == '4':
            opt.alterar_produto()
         
        elif entrada == '0':
            break
        else:
            print('erro')



