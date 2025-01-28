def triangulos():
    lado_1 = float(input(f'Digite o primeiro lado do triângulo: '))
    lado_2 = float(input(f'Digite o segundo lado do triângulo: '))
    lado_3 = float(input(f'Digite o terceiro lado do triângulo: '))
    if lado_1 + lado_2 > lado_3 and lado_2 + lado_3 > lado_1 and lado_1 + lado_3 > lado_2:
        print(f'Os lados digitados formam um triângulo. ')

        if lado_1 == lado_2 == lado_3:
                print (f'O triângulo de lados {lado_1}, {lado_2} e {lado_3} é equilátero.')
        elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
                print (f'O triângulo de lados {lado_1}, {lado_2} e {lado_3} é isóceles.')
        else:
                print(f'O triângulo de lados {lado_1}, {lado_2} e {lado_3} é escaleno.')
    else:
        print(f'Os lados digitados não formam um triângulo.')

           
   

triangulos ()



