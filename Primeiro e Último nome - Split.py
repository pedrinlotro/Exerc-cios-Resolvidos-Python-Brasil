def inserir_nome():
    nome = str(input(f'Digite seu nome completo: '))
    return nome

def primeiro_nome(nome):
    return nome.split()[0]

def ultimo_nome(nome):
    return nome.split()[-1]

def main ():
    nome = inserir_nome()
    primeiro_nome_var = primeiro_nome(nome)
    segundo_nome_var = ultimo_nome(nome)
    return print(f'O primeiro nome de {nome} é {primeiro_nome_var}, e o último é {segundo_nome_var}')

main ()

