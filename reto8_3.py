i:int
n:int=int(input("numero desde el cual iniciara la cuenta: "))
if n/2!=n//2:
    n=n-1
for i in range(n,1,-2):
    print(i)