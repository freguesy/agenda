from Agenda import*

class Menu:
    def __init__(self):
        agenda = agenda()
        
        
        while True:
            entrada = input('1 - Novo Contato\n2 - Listar Contatos\n0 - Sair')
            if entrada == '1':
                agenda.salvar_contatos()

            elif entrada == '2':
                agenda.Listar_contatos()

            elif entrada == '3':
                agenda.mudar_contato()

            elif entrada == '0':
                break
            else:
                print('erro')



