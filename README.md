# Reto-8
Reto numero 8 programacion de computadoras

## Ejercicio 1
Imprimir los numeros del 1 al 100 cada uno con su respectivo cuadrado
```python
i:int
for i in range(1,101):
    print(i)
    print(i**2)
```
- Declaramos una variable llamada "i", esta se usara para representar el numero que se estara imprimiendo
- Usamos un bucle for el cual vaya haciendo pasar i por los valores del 1 al 100, dentro de este le pedimos imprimir el valor actual de i y su cuadrado
- Esto se repetira hasta que i llege a 100 (el rango esta en 101 al ser abierto), saliendose del ciclo y terminando el proceso
## Ejercicio 2
Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```python
i:int
n:int
for i in range(1,1000,2):
    print(i)
for n in range (2,1001,2):
    print(n)  
```
- Declaramos 2 variables (i y n) las cuales representaran los numeros impares y pares respectivamente
- Aplicamos un ciclo for para i que la haga pasar en el rango de 1 a 999 aumentando de a 2 el valor, de esta forma el valor nunca llegara a ser par porque impar+2= impar
- Esto se repetira hasta que i llegue a 999 (el rango es 1000 al ser abierto), saliendo del ciclo y terminando el proceso
- Aplicamos justo despues otro ciclo for en n que le haga pasar en el rango de 2 a 1000 aumentando de a 2 el valor, de esta forma el valor nunca sera impar porque par+2=par
- Esto se repetira hasta que n llegue a 1000 (el rango es 1001 al ser abierto), saliendo del ciclo y terminando el proceso
## Ejercicio 3
Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```python
i:int
n:int=int(input("numero desde el cual iniciara la cuenta: "))
if n/2!=n//2:
    n=n-1
for i in range(n,1,-2):
    print(i)
```
- Declaramos una variable i la cual representara el numero par y otro ingresable por teclado el cual representara el numero desde el cual se empezara a imprimir numero pares
- Creamos un condicional if el cual evalue si el numero es par, en caso de que no sea (comprobable a partir de comparar la igualdad de su division y su division exacta) entrara en el condicional donde se le disminuira 1 para que el numero sera par
- En caso de salir del condicional o en caso de ser un numero par se aplicara un bucle for, este hara pasar i por todos los numeros desde n hasta 2, disminuyendo en 2 el valor de i por cada paso del bucle. Dentro del bucle se imprime el valor actual de i
- Esto resultara en que se impriminan los numeros pares, bajando de n (o n-1 si n era impar) hasta 2.
## Ejercicio 4
Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```python
n:int=int(input("numero al que se quiere que llege la cuenta"))
for i in range(1,n+1):
    o:int=i
    factor:int=o
    while o>1:
        factor= factor*(o-1)
        o=o-1
    print("factorial de "+ str(i) + " es "+ str(factor))
```
- Declaramos una variable la cual represente el numero hasta el que se contara, esta variable debe ser introducida por teclado.
- Aplicamos un ciclo for que haga pasar un valor desde 1 hasta n
- Dentro de este bucle se declarara una variable o el cual sera igual a i y una variable llamada factor la cual sera inicializada con el valor de o
- Dentro del ciclo for aplicamos un while que funcionara siempre que o sea igual a 1, dentro de este el valor de facto cambiara por el valor de factor actual multiplicado por o-1
- Adicionalmente al final del ciclo se le restara 1 al valor de o
- De esta forma salidos del ciclo while tendremos una variable factor equivalente a i.(i-1).(i-2)..., realizando la misma operacion de los factoriales
- Justo despues de nuestro ciclo while se imprimira un mensaje mostrando el numero actual de i y su factorial
- Esto se repetira con todos los valores de i hasta n
## Ejercicio 5
Calcular el valor de 2 elevado a la potencia n usando ciclos for.
```python
n:int=int(input("Ingrese el exponente por el que se quiere potenciar 2: "))
resultado:int=1
for i in range (n):
    resultado *= 2
print("la potencia de 2 a la "+str(n)+" es " + str(resultado))
```
- Creamos una variable n ingresable por teclado que representara nuestro exponente y un valor "resultado" que representaa el resultado de la potencia de 2 el cual se iniciara en 1
- aplicamos un ciclo for en el cual un 1 avance desde 1 hasta n por cada iteracion, dentro de este se cambiara el valor de resultado por su valor actual por 2
- De esta forma resultado ira subiendo a 2 cuando i=1, 4 cuando i=2, 8 cuando i=3, demostrando entonces que n efectivamente es igual al exponente
- Acabado el ciclo for se imprimira el resultado de la potencial
## Ejercicio 6
Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
```python
n:int=int(input("Ingrese el exponente: "))
x: float=float(input("Ingrese el numero que quiere potenciar: "))
resultado:int=1
for i in range (n):
    resultado *= x
print("la potencia de "+ str(x)+" a la "+str(n)+" es " + str(resultado))
```
- Se crea 2 variables n y x las cuales podran ser introducibles por teclado, estas representaran el exponente y la base respectivamente.
- Se crea una variable resultado la cual representara el resultado de nuestra potencia
- Realizamos el mismo proceso del ejercicio 5, pero esta vez en vez de multiplicarse el valor de resultado actual por 2 se multiplicara por nuestro valor x.
- De esta forma por cada iteracion el numero sera igual a  x cuando i=1, x*x cuando i=2 hasta i**n cuando i=n
- Hecho el ciclo se imprimira el resultado de la potencia
## Ejercicio 7
Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
```python
n:int
i:int 
for n in range(0,10):
    print("tabla del "+str(n)+" :")
    for i in range(0,11):
        print(n*i)
```
- Se declara una variable n la cual representara la tabla y una variable i la cual representara los diferentes valores de la tabla
- Se aplica un bucle for donde n ira desde 0 hasta 9 dentro del cual se imprimira un mensaje diciendo el numero actual de la tabla para seguido a esto aplicar otro ciclo for
- Este segundo ciclo for ira desde 0 hasta 10, imprimiendo por cada iteracion la multiplicacion entre i y n
- De esta forma debajo de cada mensaje de "tabla del n:" tendremos los productos de este numero por los valores de i desde el 0 hasta el 10
## Ejercicio 8
Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
```python
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

```
- Importamos el paquete math para tener a mano la funcion exponencial real, esto con el fin de comparar con su aproximancion
- Creamos variables que representen el valor de x, numero de terminos de la sumatoria (ambas ingresables por teclado), una tercera variable o inicializada en 1 y una variable que represente el valor real de la funcion exponencial en x
- Imprimimos el valor real de la funcion exponencial en x, aplicando justo debajo un bucle for para un valor i el cual vaya desde 1 hasta n
- Dentro de este valor por cada iteracion declararemos un valor factor inicializado en i y otro valor u que tambien este inicializado en i
- Declaras estas variables aplicamos un ciclo while donde usaremos el proceso para generar un factorial, en este caso el factorial de nuestro valor i
- justo despues de nuestro ciclo while para transformar nuestra variable factor en el factorial de i volvemos a declarar o, esta vez haciendola igual a su valor actual mas x potenciado a i entre factor
- Lo que se realizo con esto fue emular la operacion de la sumatoria dada, de esta forma  cuando nuestro ciclo for acabe o sera igual a la aproximacion de la funcion exponencial
- Justo despues del ciclo for imprimimos el valor resultante de o, de esta forma siendo capaces de hacer una comparacion visual entre el valor real(el cual estara justo arriba) y el valor aproximado (o)
- Creamos una variable llamada "cate" la cual sea igual a la resta entre el valor real y el aproximado
- Dividimos este valor "cate" entre  el valor real y lo multiplicamos por 100, obteniendo asi su porcentaje dentro de una variable llamada agua
- Usamos un condicional if-else para evaluar si "agua es menor o mayor/igual a 0.1%, si es el primer caso se informara por medio de un print que la aproximacion es buena. En caso contrario diremos que no lo es"
## Ejercicio 9
Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

```python
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
```
- Importamos el paquete math para tener a mano la funcion seno exacta, esto con el fin de comparar con su aproximancion
- Creamos variables que representen el valor de x, numero de terminos de la sumatoria (ambas ingresables por teclado), una tercera variable "o" inicializada en x y una variable que represente el valor real de la funcion seno en x
- Imprimimos el valor real de la funcion seno en x, aplicando justo debajo un bucle for para un valor i el cual vaya desde 1 hasta n
- Dentro de este valor por cada iteracion declararemos un valor a inicializado como 2i+1, un valor factor inicializado en 2i+1 y un valor u inicializado en a
- Declaradas estas variables aplicamos un ciclo while donde usaremos el proceso para generar un factorial, en este caso el factorial de nuestro valor 2i+1
- justo despues de nuestro ciclo while para transformar nuestra variable factor en el factorial de 2i+1 declaramos diferentes variables que al juntaras en una variable m sean igual a la ecuacion de la aproximacion de la funcion seno (-1 a la i por x a la 2i+1 ente factor de 2i+1), esta variable sera sumada con "o" para formar el nuevo valor resultante de o el cual sera igua a la aproximacion
- Lo que se realizo con esto fue emular la operacion de la sumatoria dada, de esta forma  cuando nuestro ciclo for acabe o sera igual a la aproximacion de la funcion seno
- Justo despues del ciclo for imprimimos el valor resultante de o, de esta forma siendo capaces de hacer una comparacion visual entre el valor real(el cual estara justo arriba) y el valor aproximado (o)
- Creamos una variable llamada "cate" la cual sea igual a la resta entre el valor real y el aproximado
- Dividimos este valor "cate" entre  el valor real y lo multiplicamos por 100, obteniendo asi su porcentaje dentro de una variable llamada agua
- Usamos un condicional if-else para evaluar si "agua es menor o mayor/igual a 0.1%, si es el primer caso se informara por medio de un print que la aproximacion es buena. En caso contrario diremos que no lo es"
## Ejercicio 10
Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
```python
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
```
- En este caso gracias al haber realizado el proceso con la funcion seno anteriormente simplemente necesitamos hacer unos pocos cambios:
- en vez de importar la funcion seno importamos la funcion arco tangente
- al ingresar x antes de seguir se aplica un condicional que nos compruebe esta no esta fuera del rango [-1,1], si esto si esto no es asi se continuara el codigo, pero si lo es se terminara
- en nuestra variable m (conocida en este codigo como z) en vez de que toda la funcion sea divida por el factor de 2i+1 lo cambiamos por 2i+1 sin mas
- El restro del proceso es el mismo
