n=int(input())
a=list(map(int,input().split()))
s1,s2=0,0
for i in a:
    if i%2==0: s1+=i
    else: s2+=i
print(abs(s1-s2))