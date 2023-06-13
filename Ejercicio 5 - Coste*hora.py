# Escribir un programa que pregunte al usuario por el número de
  horas trabajadas y el coste por hora. Después debe mostrar por
  pantalla la paga que le corresponde.

horas = float(input("Número de horas trabajadas: "))
coste = float(input("Coste por hora: "))
print (f"Tu paga es de {coste*horas}€")
