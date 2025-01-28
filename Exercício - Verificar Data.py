def verificar_data():
    data = (input(f'Digite a data no formato dd/mm/aaaa: '))
    try:
        dia, mes, ano = map(int, data.split('/'))
        if ano < 1:
            print(f'O ano digitado é inválido.')
            return
        if mes < 1 or mes > 12:
            print(f'O mês digitado é inválido.')
    
        dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            dias_no_mes[1] = 29

        if dia < 1 or dia > dias_no_mes[mes - 1]:
            print("Dia inválido.")
        else:
            print("A data digitada é válida.")

    except ValueError:
        print("Formato inválido. Certifique-se de usar o formato dd/mm/aaaa.")

verificar_data ()