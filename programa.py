from dados import *
arq = 'cadastros_formulario.txt'
titulo('MENU PRINCIPAL - DOWNLOAD E-BOOK "SAUDÁVEL E EM FORMA"', 'Preencha o seu cadastro e obtenha o seu e-book')
print()
usuario = Usuario()
resp = menu('Cadastrar', 'Consultar', 'Finalizar')
while True:
    if resp == 1:
        titulo('opção 1')
        usuario.cadastro()
        titulo('MENU')
    if resp == 2:
        titulo('Digite o login e senha para acessar a Área Restrita ou 999 para encerrar.',
               'Senha disponível no READ ME.')
        print('\n')
        try:
            login = int(input(f'{"":<45}{"Login: "}'))
            senha = int(input(f'{"":<45}{"Senha: "}'))
            print('\n')
        except:
            print(f'Apenas números.\n'.center(150))
        else:
            if login == 1234 and senha == 1234:
                titulo('opção 2')
                print('\n')
                mostrar_listagem(arq, 'código', 'nome', 'idade', 'imc')
                pesq = pesquisa(arq)
                if pesq == 999:
                    print()
            elif login == 999 and senha == 999:
                break
            else:
                print('Login ou Senha inválido.')
    if resp == 3:
        print('\nPrograma Finalizado.'.center(50))
        break