def crescimento():
   anos = 0
   while True:
      try:
        pop_a = int(input(f'Digite a quantidade da população A'))
        if pop_a > 0:
            print(f'População A válida.')
            break
        else:
           print (f'A população deve ser maior do que 0.')
      except ValueError:
        print(f'Input inválido')
    
   while True:
        try:
           pop_b = int(input(f'Digite a quantidade da população B'))
           if pop_b > 0:
              print(f'População B válida.')
              break 
           else:
              print(f'A população deve ser maior do que 0.')
        except ValueError:
            print(f'Input inválido.')

   while True:
        try:
           taxa_crescimento_a = float(input(f'Digite a taxa de crescimento anual da população A'))
           if taxa_crescimento_a > 0:
              print(f'Taxa de crescimento válida.')
              break 
           else:
              print(f'A taxa de crescimento deve ser maior do que 0.')
        except ValueError:
            print(f'Input inválido.')

   while True:
        try:
           taxa_crescimento_b = float(input(f'Digite a taxa de crescimento anual da população B'))
           if taxa_crescimento_b > 0:
              print(f'Taxa de crescimento válida.')
              break 
           else:
              print(f'A taxa de crescimento deve ser maior do que 0.')
        except ValueError:
            print(f'Input inválido.')

   while pop_a < pop_b:
      pop_a = pop_a + (pop_a * taxa_crescimento_a)
      pop_b = pop_b + (pop_b * taxa_crescimento_b)
      anos = anos + 1

   print (f'Serão necessários {anos} anos')

crescimento()
