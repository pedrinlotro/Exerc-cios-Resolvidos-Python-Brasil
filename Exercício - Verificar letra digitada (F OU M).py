def main():
    letra = input(f'Digite "m" para masculino ou "f" para feminino : ')
    if letra.lower() == "m":
        print(f'Você é do sexo Masculino.')
    elif letra.lower() == "f":
        print(f'Você é do sexo Feminino.')
    else:
        print(f'Sexo inválido.')

main ()