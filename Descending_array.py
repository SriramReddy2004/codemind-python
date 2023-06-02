n=int(input())
a=list(map(int,input().split()))
b=a.copy()
b.sort(reverse=True)
if a==b:
    print("yes")
else:
    print("no")