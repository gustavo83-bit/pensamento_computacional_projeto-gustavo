def saudar(nome):
    print(f"Olá, {nome}! Bem-vindo ao mundo da programação.")

saudar("Tiago")
saudar("Maria")


def realizar_login():
    print('\n--- Tela de login - Meet ---')
    
    nome_usuario = input('Digite seu login para continuar: ')
    senha_usuario = input('Digite sua senha para continuar: ')
    
    print(f'Bem-vindo, {nome_usuario}!')
    print('---------------------------\n')

realizar_login()


import getpass

def realizar_login_com_invisivel():
    senha_padrao = "vocacao2025"
    
    print('\n--- Sistema de Login Protegido ---')
    nome_usuario = input('Digite seu login: ')

    senha_digitada = getpass.getpass('Digite sua senha (não aparecerá): ')

    if senha_digitada == senha_padrao:
        print(f'\n[SUCESSO] Bem-vindo, {nome_usuario}!')
    else:
        print('\n[ERRO] Senha incorreta!')
    
    print('----------------------------------\n')

realizar_login_com_invisivel()


def realizar_login_com_tentativas():
    senha_padrao = "vocacao2025"
    tentativas_restantes = 3
    login_sucesso = False

    print('\n--- Sistema de Login (máx. 3 tentativas) ---')
    nome_usuario = input('Digite seu login: ')

    while tentativas_restantes > 0 and not login_sucesso:
        print(f'\nTentativas restantes: {tentativas_restantes}')
        senha_digitada = getpass.getpass('Digite sua senha: ')

        if senha_digitada == senha_padrao:
            print(f'\n[SUCESSO] Bem-vindo, {nome_usuario}!')
            login_sucesso = True
        else:
            tentativas_restantes -= 1
            if tentativas_restantes > 0:
                print('[ERRO] Senha incorreta. Tente novamente.')
            else:
                print('\n[BLOQUEADO] Número de tentativas excedido!')

    print('--- Fim da operação ---\n')

realizar_login_com_tentativas()