import math
sen=math.sin
x:float=float(input("ingrese el valor de x:"))
n:int=int(input("ingrese el numero de terminos a sumar: "))
expresion=sen(x)
print(expresion)
o:int=x
for i in range(1,n+1): 
    a=(2*i)+1
    u:int=a
    factor:int=(2*i)+1
    while u>1:
        
        factor= factor*(u-1)
        u=u-1
    z=((-1)**i)
    q=(x**a)
    m=z*q/factor
    o=o+(m)
print(o)
print("Hay una diferencia de "+str(expresion-o))
cate=expresion-o
agua=(cate/expresion)*100
if agua<0.1:
    print("El error relativo es: "+str(agua)+"% (debajo del 0.1%). Es una buena aproximacion")
else:
    print("El error relativo es: "+str(agua)+"% (arriba del 0.1%). No es una buena aproximacion")