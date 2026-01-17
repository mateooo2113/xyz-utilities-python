from math import pi 


print("-----------------------------------------------")
print("Bienvenido al sistema de la empresa XYZ :)")

print("           Empresa XYZ")
print("----------------------------------")

print("1.Control de Temperatura")
print("2.Calcular Salario")
print("3.Calcular Áreas y Perímetros")
print("4.Salir")
acc = input("Seleccione el numeral de la acción a realizar: ")

if acc == "1": 
    print("----------------------------------")
    print("         Temperatura")
    temp = int(input("Ingrese la temperatura que marca el termostato: "))

    if temp > 30:
        print("Temperatura MUUUUY alta, enfriando antes de derretirse")
        print("----------------------------------")

    elif temp < 15:
        print("Temperatura DEMASIADO baja, te vas a congelar")
        print("Se subirá la temperatura")
        print("----------------------------------")

    elif temp < 21:
        print("Temperatura baja")
        print("Se subirá la temperatura")
        print("----------------------------------")

    elif temp > 24:
        print("Temperatura alta")
        print("Se bajará la temperatura")
        print("----------------------------------")

    else: 
        print("Temperatura aceptable, disfruta el día :)")
        print("----------------------------------")

elif acc == "2":
    print("----------------------------------")
    salario = float(input("Ingrese su Salario Mensual: "))
    salariosem = salario / 4
    salariodia = salariosem / 5
    salariohora = salariodia / 8 

    print("Su salario semanal es: ", salariosem)
    print("Su salario diario es : ", salariodia)        
    print("Su salario por hora es: ", salariohora)
    print("----------------------------------")

elif acc == "3": 
    print("----------------------------------")
    print("Áreas y Perímetros")
    print("1. Círculo")
    print("2. Cuadrado")
    print("3. Triángulo")
    print("4. Rectángulo")
    fig = input("Seleccione una figura: ")

    if fig == "1":
        med = input("¿Tiene el diámetro o el radio?: ")
        

        if med == "radio":
            rad = int(input("Ingrese el radio: "))
            areacir = pi * (rad ** 2)
            perimcir = 2 * pi * rad
            print("El área es : ", areacir)
            print("El perímetro es : ", perimcir)

        else:
            diam = int(input("Ingrese el diámetro: "))
            areacir = pi * (diam / 2) ** 2
            perimcir = 2 * pi * (diam / 2)
            print("El área es : ", areacir)
            print("El perímetro es : ", perimcir)

    elif fig == "2":
        lado = int(input("Ingrese la medida de un lado: "))
        areacuad = lado * lado
        perimcuad = lado * 4
        print("El área es : ", areacuad)
        print("El perímetro es : ", perimcuad)

    elif fig == "3":
        base = int(input("Ingrese el valor de la base: "))
        altura = int(input("Ingrese el valor de la altura: "))
        lad1 = int(input("Ingrese el valor del lado 1: "))
        lad2 = int(input("Ingrese el valor del lado 2: "))
        lad3 = int(input("Ingrese el valor del lado 3: "))

        perimtrian = lad1 + lad2 + lad3
        areatrian = (base * altura) / 2

        print("El área es : ", areatrian)
        print("El perímetro es : ", perimtrian)

    else:
        baserec = int(input("Ingrese la base: "))
        alturarec = int(input("Ingrese la altura: "))

        arearec = baserec * alturarec
        perimetrorec = (baserec * 2) + (alturarec * 2)

        print("El área es : ", arearec)
        print("El perímetro es : ", perimetrorec)

else: 
    print("Salió del menú")



