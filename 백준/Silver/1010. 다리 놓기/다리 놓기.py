import math

t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    num=1
    for j in range(n):
        num*=m
        m-=1
    num=int(num/math.factorial(n))
    print(num)
