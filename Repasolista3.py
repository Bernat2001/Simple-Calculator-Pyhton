Asignaturas=["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
scores= []
for Asignatura in Asignaturas:
    score = input("¿Que nota has sacado en " + Asignatura +"?")
    scores.append(score)
    for i in range(len(Asignaturas)):
        print("En " + Asignaturas[i] + scores[i])
    break






    