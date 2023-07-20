def titulo(tit='', subtitulo=''):
    print('\033[7;37m-' * 150, '\033[m')
    print('\033[7;37m', tit.strip().center(149).upper(), '\033[m')
    print('\033[7;37m-' * 150, '\033[m')
    if subtitulo != '':
        print(subtitulo.strip().center(150), '\n')


def menu(*op):
    opcoes = []
    for i, p in enumerate(op):
        opcoes.append(p)
        print(f'{i+1} - {p}'.center(100))
    print()
    while True:
        try:
            resposta = int(input(f'{"":<10}Sua opção: '))
            if 0 < resposta <= len(opcoes):
                return resposta
            else:
                print('Digite uma opção válida.'.center(150))
        except KeyboardInterrupt:
            break
        except:
            print('Digite uma opção válida.'.center(150))


def alerta_erro(erro):
    return print(f'\033[;31m{erro}\033[m')


def menu_dados(*dados):
    opcoes = []
    for i in dados:
        pergunta = str(input(i))
        if pergunta.isnumeric():
            numero = int(pergunta)
            opcoes.append(numero)
        else:
            opcoes.append(pergunta)
    return opcoes


