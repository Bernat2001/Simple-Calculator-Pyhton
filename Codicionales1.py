print("Programa de evalucion de notas")


nota_alumno= input("Dime tu nota: ")

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="Suspenso"
    return valoracion


print(evaluacion(int(nota_alumno)))

        