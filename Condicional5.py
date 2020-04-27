print("Asignaturas optativas 2020")
print("Asignaturas optativas: Informatica grafica - Pruebas de Software - Usabilidad y Accesibilidad")
opcion=input("Escribe la asignatura esogida: ")

asignatura=opcion.lower()

if asignatura in ("informatica grafica",  "pruebas de software", "usabilidad y accesibilidad"):

    print("Asignatura elegida " + asignatura)

else:

    print("La asignatura escogida no esta disponible")