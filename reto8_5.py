n:int=int(input("Ingrese el exponente por el que se quiere potenciar 2: "))
resultado:int=1
for i in range (n):
    resultado *= 2
print("la potencia de 2 a la "+str(n)+" es " + str(resultado))

