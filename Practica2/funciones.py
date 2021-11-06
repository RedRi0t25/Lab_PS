def funcion(n1, n2):
    operacion = int(n1) + int(n2)
    print (operacion)

    if operacion>0:
        print("Tu resultado es positivo")
    else:
        print("Tu resultado es negativo")

funcion(input("primer numero: "),input("segundo numero: "))
        
c = input("¿quieres hacer otra suma? presiona Y si es asi").lower()

while c == 'y':
    funcion(input("primer numero: "),input("segundo numero: "))
    c = input("¿quieres hacer otra suma? presiona Y si es asi").lower()
    

    



