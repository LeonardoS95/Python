def regis():
    try:
        arquivo = open('dados.txt')
        arquivo.close()
    except FileNotFoundError:
        arquivo = open('dados.txt', 'w')
        print(f'\033[32mArquivo {arquivo.name} criado com sucesso!\033[m')


def ler(num):
    if num == 1:
        arquivo = open('dados.txt', 'r')
        for dado in arquivo:
            print(dado.replace('\n', ''))
        arquivo.close()


def escreve():
    nome = str(input('Nome: ')).strip()
    if nome == '':
        nome = 'Desconhecido'
    while True:
        try:
            idade = int(input('Idade: '))
        except ValueError:
            print(f'\033[31mIdade inválida! Digite novamente!\033[m')
        else:
            print(f'\033[32m{nome} cadastrado com sucesso!\033[m')
            arquivo = open('dados.txt', 'a')
            arquivo.writelines(f'{nome:<20} {idade:>2} Anos\n')
            break
