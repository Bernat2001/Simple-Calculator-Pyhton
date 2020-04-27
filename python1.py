print("Esto es una calculadora")
print("-----------------------")

numero1=(int(input("Escribe el primer numero: ")))

print("-----------------------")

print("Elige entre: ")

print("+")
print("-")
print("*")
print("/")
print("**")

metodo=(str(input("Escribe el metodo de la operación: ")))
print("-----------------------")
numero2=(int(input("Escribe el segundo numero: ")))
print("-----------------------")

if metodo==("+"):
	print(f"El resultado es: {numero1+numero2}")
	print("Gracias por utilizar la calculadora")

if metodo==("-"):
	print(f"El resultado es: {numero1-numero2}")
	print("Gracias por utilizar la calculadora")

if metodo==("*"):
	print(f"El resultado es: {numero1*numero2}")
	print("Gracias por utilizar la calculadora")

if metodo==("/"):
	print(f"El resultado es: {numero1/numero2}")
	print("Gracias por utilizar la calculadora")

if metodo==("**"):
	print(f"El resultado es: {numero1**numero2}")
	print("Gracias por utilizar la calculadora")

