x=1
materias=float(input("Cuantas materias tienes este semestre"))
suma=0
while x<=materias:
    valor=float(input("Ingrese calificación de la materia"))
    suma=suma+valor
    x=x+1
promedio=suma/materias
print("La suma de las materias es", suma, ".")
print("El promedio es", promedio)
