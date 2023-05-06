n=int(input())
while n>10:
    t,sum=n,0
    while t:
        sum+=t%10
        t//=10
    n=sum
print(n)