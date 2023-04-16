c = ('\033[m',      # 0 - Cor zero
     '\033[1;31m',  # 1 - Cor Vermelha
     '\033[1;32m',  # 2 - Cor Verde
     '\033[1;33m',  # 3 - Cor Amarela
     '\033[1;34m')  # 4 - Cor Azul


def titulo(txt):
    print('=' * 30)
    print(txt.center(30))
    print('=' * 30)


def lin():
    print('-' * 30)


def lista(op):
    i = 1
    for item in op:
        print(f'{c[3]}{i}{c[0]} - {c[4]}{item}{c[0]}')
        i += 1


def opcao(txt):
    while True:
        try:
            num = int(input(f'{c[3]}{txt}{c[0]}'))
        except ValueError:
            print(f'{c[1]}ERRO! Por favor digite um número inteiro válido{c[0]}')
            continue
        else:
            if num < 1 or num > 3:
                print(f'{c[1]}ERRO!Opção inválida!{c[0]}')
            else:
                return num
