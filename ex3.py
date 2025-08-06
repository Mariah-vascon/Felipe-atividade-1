def aprovaçao():
    nome = str(input('digite seu nome:'))
    idade = int(input('digite sua idade:'))
    email = str(input('digite seu email:'))
    if idade > 18 and '@' in email:
        print('cadrastro concluido com sucesso!')
    else:
        print('cadastro não realizado!')

aprovaçao()