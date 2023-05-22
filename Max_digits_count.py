n=int(input())
arr=list(map(int,input().split()))
mn=max(*arr)
mn=len(str(mn))
cnt=0
for i in arr:
    if len(str(i))==mn:
        cnt+=1
print(cnt)