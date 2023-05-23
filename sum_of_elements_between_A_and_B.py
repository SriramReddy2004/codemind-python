n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
sm=0
for i in lst:
    if i>=a and i<=b:
        sm+=i
print(sm)