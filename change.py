def change():
    expense = 23.75
    money = 100
    vuelto = money - expense

    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    print("Ingresar gasto:")
    print("23.75")
    print("Dinero recibido")
    print("100")
    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
