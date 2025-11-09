import sys,math

n,w,h=map(int,sys.stdin.readline().split())
diagonal=math.sqrt(w**2+h**2)
for i in range(n):
    m=int(sys.stdin.readline())
    if m<=diagonal:
        print("DA")
    else:
        print("NE")
