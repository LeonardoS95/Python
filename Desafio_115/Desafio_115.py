from time import sleep
from emoji import emojize
from menu import *
from cadastro import *

regis()
while True:
    titulo('MENU PRINCIPAL')
    lista(['Pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema'])
    lin()
    item = opcao('Opção: ')
    if item == 1:
        titulo('PESSOAS CADASTRADAS')
        ler(item)
    elif item == 2:
        titulo('NOVO CADASTRO')
        escreve()
    else:
        print('Saindo do programa...')
        sleep(3)
        print(emojize('Até logo :mão_acenando:', language='pt'))
        break
