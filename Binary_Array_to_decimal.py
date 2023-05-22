n=int(input())
lst=list(map(int,input().split()))
t,num=1,0
for i in lst[::-1]:
    num+=i*t
    t*=2
print(num)