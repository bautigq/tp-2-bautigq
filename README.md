[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/VFDGFHcP)
# Trabajo Práctico 2

## Ejercicio 1 - Ada

Los nombres suelen venir en distintas formas y uno siempre tiene que estar preparado para lo peor. En este caso, necesitamos ordenar y organizar un poco estos nombres. Para este task, tenes que lograr dado un nombre y un apellido, poder mostrar el nombre completo en distintos formatos. En este caso lo que necesitamos es lo siguiente: 

Dado las siguientes dos variables:

```python
first_name = "AdA"
last_name  = "LoVeLAce"
```

Lograr conseguir este mismo output: 
```python 
ada lovelace 
Ada Lovelace 
ADA LOVELACE  
	ada lovelace
```
*Codigo*
first_name = "AdA"
last_name = "LoVeLAce"

print(first_name.lower(), last_name.lower())
print(first_name.capitalize(), last_name.capitalize())
print(first_name.upper(), last_name.upper())
print("\t" + first_name.lower(), last_name.lower())



## Ejercicio 2 - Earth

El planeta tierra es muy grande y actualmente es el hogar de 7700 millones de personas. Las personas viven en distintos paises y necesitamos distinguir las ubicaciones una de otra.

En este ejercicio, necesitamos saber qué país esta primero en el diccionario. Dado los paises Bangladesh y Barbados, comparar los paises teniendo en cuenta quien esta primero en el diccionario.

La respuesta debería tener el siguiente formato (Donde X es Bangladesh e Y es Barbados):

```python
The result of X comes first in the dictionary than Y is True/False.
The result of Y comes first in the dictionary than X is True/False.
```
*Codigo*
country1 = "Bangladesh"
country2 = "Barbados"

result1 = country1 < country2
result2 = country2 < country1

print(f"The result of {country1} comes first in the dictionary than {country2} is {result1}.")
print(f"The result of {country2} comes first in the dictionary than {country1} is {result2}.")


## Ejercicio 3 - Change

Escribir un programa que dado dos números reales que representan el gasto efectuado por una persona y la cantidad pagada, imprima en pantalla el informe de la cantidad de pesos y centavos a devolver.

Hay que respetar el formato del informe (incluido la prolijidad con los espacios y saltos de linea). Un ejemplo de un informe es:

```python
Ingresar gasto:
23.75
Dinero recibido
100

Vuelto

Pesos:
76
Centavos:
25
```
*Codigo*
gasto = float(input("Ingresar gasto:\n"))
pago = float(input("Dinero recibido\n"))

vuelto = pago - gasto
pesos = int(vuelto)
centavos = int(round((vuelto - pesos) * 100))

print("\nVuelto\n")
print("Pesos:")
print(pesos)
print("Centavos:")
print(centavos)
