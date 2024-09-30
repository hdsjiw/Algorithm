n=int(input())
a,b=map(int,input().split())
drinks=int(a/2)+b
if drinks<=n:
    print(drinks)
else:
    print(n)