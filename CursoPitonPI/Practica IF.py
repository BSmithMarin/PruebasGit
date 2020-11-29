print("Programa de evaluacion")
nota_alumno=int(input("introduce la nota del alumno:"))

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion


print(evaluacion(nota_alumno))