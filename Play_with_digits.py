n=int(input())
a=list(map(str,input().split()))
b=[]
for i in a:
    b.extend(i)
s=0
for i in b:
    s+=int(i)
print(s)