k=int(input())
a,b,c,d=map(int,input().split())

if a*k+b==c*k+d:
    print("Yes",end=" ")
    print(a*k+b)
else:
    print("No")