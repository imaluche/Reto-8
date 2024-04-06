n:int=int(input("Ingrese el exponente: "))
x: int=int(input("Ingrese el numero que quiere potenciar: "))
resultado:int=1
for i in range (n):
    resultado *= x
print("la potencia de "+ str(x)+" a la "+str(n)+" es " + str(resultado))