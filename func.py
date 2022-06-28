from infos import*

class funço:
    def __init__(self):
        self.listaProdutos = []

    def salvar_produtos(self):
        self.listaProdutos.append(Informações())

    def listar_produtos(self):
        for i in range(len(self.listaProdutos)):
            print ('\nCódigo -',self.listaProdutos[i].cod,'\nNome -', self.listaProdutos[i].descrição,'\nFabricante -' ,self.listaProdutos[i].fabricante,'\nQuantidade -' ,self.listaProdutos[i].quantidade,'\n')

    def alterar_produto(self):
        b = input("buscar o produto por nome para mudar")
        for i in range(len(self.listaProdutos)):
            if b == self.listaProdutos[i].cod:
                self.listaProdutos[i].descrição = input('Digite o novo número')
