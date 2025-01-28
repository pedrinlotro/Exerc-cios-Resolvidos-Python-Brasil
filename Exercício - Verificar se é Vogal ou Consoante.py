def main():
    vogais = ["a", "e", "i", "o", "u"]
    letra = input(f'Digite uma letra: ')
    if letra.lower() in vogais:
        print(f'A letra {letra} é uma vogal')
    else:
        print(f'A letra {letra}, é uma consoante')

main()
        
