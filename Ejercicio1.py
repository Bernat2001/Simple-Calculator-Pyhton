num1=int(input("Dime num1: "))

num2=int(input("Dime num2: "))

def DevuelveMax(n1, n2):

    if n1 < n2:
        print(n2)
    elif n2 < n1:
        print(n1)
    else:
        print("Son iguales")

DevuelveMax(num1, num2)





