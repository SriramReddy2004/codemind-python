n1=int(input())
n2=int(input())
def isPrime(n):
    c=0
    for i in range(2,n):
        if n%i==0: c+=1
    return c==0
n3=n1+n2+1
while not isPrime(n3): n3+=1
print(n3-n2-n1)