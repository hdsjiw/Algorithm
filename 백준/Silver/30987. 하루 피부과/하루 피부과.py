x1,x2=map(int,input().split())
a,b,c,d,e=map(int,input().split())

strong=(a//3)*(x2**3-x1**3)+((b-d)//2)*(x2**2-x1**2)+(c-e)*(x2-x1)

print(int(strong))
