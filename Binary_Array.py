n=int(input())
lst=list(map(int,input().split()))
print((lst.count(0)+lst.count(1))==n)