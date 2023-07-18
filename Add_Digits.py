n=int(input())
s=10
while s>9:
    s=0
    while n:
        s+=n%10
        n//=10
    n=s
print(s)