

n:int=int(input("numero al que se quiere que llege la cuenta"))
for i in range(1,n+1):
    o:int=i
    factor:int=o
    while o>1:
        factor= factor*(o-1)
        o=o-1
    print("factorial de "+ str(i) + " es "+ str(factor))