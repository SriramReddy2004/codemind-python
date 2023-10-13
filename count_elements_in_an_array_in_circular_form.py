n=int(input())
a=list(map(int,input().split()))
c=0
for j in range(n):
    if a[j]%2^a[(j+2)%n]%2:
        c+=1
print(c)