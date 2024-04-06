import math
arctan=math.atan
x:float=float(input("ingrese el valor de x(debe estar en el intervalo [-1,1]):"))
if x>1 or x<-1:
    print("el valor de x no esta en el intervalo [-1,1]")
    exit()
n:int=int(input("ingrese el numero de terminos a sumar: "))
expresion=arctan(x)
print(expresion)
o:int=x
for i in range(1,n+1): 
    a=(2*i)+1
    u:int=a
    factor:int=(2*i)+1
    while u>1:
        
        factor= factor*(u-1)
        u=u-1
    z=(((-1)**i)*(x**a))/a
    o=o+(z)
print(o)
print("Hay una diferencia de "+str(expresion-o))
cate=expresion-o
agua=(cate/expresion)*100
if agua<0.1:
    print("El error relativo es: "+str(agua)+"% (debajo del 0.1%). Es una buena aproximacion")
else:
    print("El error relativo es: "+str(agua)+"% (arriba del 0.1%). No es una buena aproximacion")