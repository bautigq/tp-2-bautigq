def change():
    expense = 23.75
    money = 100
expense = float(input("Ingresar expense:\n")) 
money = float(input("Dinero recibido\n"))

vuelto = money - expense 
pesos = int(vuelto) 
centavos = int(round((vuelto - pesos) * 100))

print("\nVuelto\n") 
print("Pesos:") 
print(pesos) 
print("Centavos:") 
print(centavos)
