a=int(input())
b=int(input())
def isprime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
    return c==0
for i in range(a+1,b):
    if isprime(i):
        print(i)