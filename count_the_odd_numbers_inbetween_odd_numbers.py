n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(n-2):
    if a[i]%2 & a[i+1]%2 & a[i+2]%2:
        cnt+=1
print(cnt)