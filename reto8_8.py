import math
exp=math.exp
x:int=int(input("ingrese el valor de x:"))
n:int=int(input("ingrese el numero de terminos a sumar: "))
o:int=1
expresion=exp(x)
print(expresion)
for i in range(1,n+1):
    factor:int=i
    u:int=i
    while u>1:
        factor= factor*(u-1)
        u=u-1
    o=o+(x**i)/factor
print(o)
print("Hay un diferencia de "+str(expresion-o))
cate=expresion-o
agua=(cate/expresion)*100
if agua<0.1:
    print("El error relativo es: "+str(agua)+"% (debajo del 0.1%). Es una buena aproximacion")
else:
    print("El error relativo es: "+str(agua)+"% (arriba del 0.1%). No es una buena aproximacion")
