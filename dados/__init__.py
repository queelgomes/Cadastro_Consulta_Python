from datetime import datetime
from interfaces import *


def arquivo_existe(nome_arquivo):
    try:
        arq = open(nome_arquivo, 'rt')
        arq.close()
    except:
        criarArquivo(nome_arquivo)


def criarArquivo(nome_arquivo):
    arq = open(nome_arquivo, 'wt+')
    arq.close()


def lerArquivo(nome_arquivo):
    arq = open(nome_arquivo, 'rt')
    lista_dados = []
    dados_usuarios = {}
    for i, linha in enumerate(arq):
        dados_usuarios['código'] = i
        linha = linha.replace("(", '')
        linha = linha.replace("'", '')
        linha = linha.replace(")\n", '')
        dados = linha.split(', ')
        for x in range(0, len(dados), 2):
            dados_usuarios[dados[x]] = dados[x + 1]
        lista_dados.append(dados_usuarios.copy())
    return lista_dados


def mostrar_listagem(nome_arquivo, *menus):
    lista = lerArquivo(nome_arquivo)
    print(f'{"":<40}', end='')
    for indices in menus:
        if indices == 'nome':
            print(f'{indices.upper():<40}', end='')
        elif indices == 'código':
            print(f'{"CÓD":<6}', end='')
        else:
            print(f'{indices.upper():<15}', end='')
    print()
    for l in lista:
        print(f'{"":<40}', end='')
        for m in menus:
            if m == 'nome':
                print(f'{l[m]:<40}', end='')
            elif m == 'código':
                print(f'{l[m]:<6}', end='')
            else:
                print(f'{l[m]:<15}', end='')
        print()


def pesquisa(nome_arquivo):
    arq = lerArquivo(nome_arquivo)
    while True:
        try:
            pesq = int(input(f'\n{"":>15}Digite o código desejado ou 999 para voltar: '))
            if pesq <= len(arq):
                for i in range(0, len(arq)):
                    for k, v in arq[i].items():
                        if k == 'código' and v == pesq:
                            titulo(f'pesquisa detalhada')
                            print()
                            print()
                            for keys, values in arq[i].items():
                                print(f'{"":<45}{f"{keys.upper()}":.<20} {values}')
            elif pesq == 999:
                return 999
            else:
                print('Código não consta na listagem.')
        except KeyboardInterrupt:
            break
        except:
            print('Código não consta na listagem.')


class Usuario:
    def __init__(self):
        self.__nome = 'nome'
        self.__dt_nasc = 'data de nascimento'
        self.__cidade = 'cidade'
        self.__peso = 0.0
        self.__altura = 0.0
        self.__email = 'email'
        self.__celular = 'celular'
        self.__confirma = 'confirma'

    def cadastro(self):
        self.__nome = str(input(f'{"":<45}Nome: '))
        self.__dt_nasc = str(input(f'{"":<45}Data de Nacimento: '))
        self.__retorno_dt()
        self.__cidade = str(input(f'{"":<45}Cidade: '))
        while True:
            try:
                self.__peso = float(input(f'{"":<45}Peso(kg): '))
                break
            except KeyboardInterrupt:
                break
            except:
                print(f'{"":<45}Peso inválido. Digite novamente.')
        while True:
            try:
                self.__altura = float(input(f'{"":<45}Altura(kg): '))
                break
            except KeyboardInterrupt:
                break
            except:
                print(f'{"":<45}Altura inválida. Digite novamente.')
        self.__email = str(input(f'{"":<45}E-mail: '))
        self.__celular = str(input(f'{"":<45}Celular com DDD (xx): '))
        self.__confirma = str(input(f'\n{"":<45}Confirma o cadastro? [S/N]'))
        while True:
            if self.__confirma in 'SsNn':
                if self.__confirma in 'Ss':
                    usuario = ('nome', self.__nome, 'data de nascimento', self.__retorno_dt(), 'idade',
                               self.__idade(),'cidade', self.__cidade, 'peso', self.__peso, 'altura', self.__altura,
                               'imc', self.__imc(), 'email', self.__email, 'celular', self.__celular)
                    arquivo_existe('cadastros_fomulario.txt')
                    arq = open('cadastros_fomulario.txt', 'at')
                    arq.write(f'{usuario}\n')
                    print('\n> > > > >  Cadastro Realizado com sucesso!\n')
                    break
                if self.__confirma in 'Nn':
                    print('\n> > > > >  Cadastro Cancelado.\n')
                    break
            else:
                self.__confirma = str(input('Confirma o cadastro? [S/N] '))

    def __valid_dn(self):
        data = self.__dt_nasc
        try:
            dia = int(self.__dt_nasc[:2])
            mes = int(self.__dt_nasc[3:5])
            meses_impar = [1, 3, 5, 7, 8, 10, 12]
            if len(data) == 10 and 0 < dia <= 31 and 0 < mes <= 12:
                if dia == 31:
                    for m in meses_impar:
                        if m == mes:
                            return True
                if 0 < dia <= 30:
                    return True
            else:
                return False
        except:
            return False

    def __retorno_dt(self):
        while True:
            if self.__valid_dn():
                return self.__dt_nasc
            else:
                print(f'{"":<45}Data de Nascimento inválida')
                self.__dt_nasc = str(input(f'{"":<45}Data de Nacimento: '))

    def __imc(self):
        imc = self.__peso / (self.__altura * self.__altura)
        return f'{imc:.1f}kg/m²'

    def __idade(self):
        try:
            if self.__retorno_dt():
                ano_atual = datetime.now().year
                ano_nasc = int(self.__dt_nasc[6:10])
                return ano_atual - ano_nasc
        except:
            return 'ERRO ANO'
# Programa Principal


