n,fc=int(input()),0
for i in range(1,n):
    if n%i==0:
        fc+=i
print(fc==n)