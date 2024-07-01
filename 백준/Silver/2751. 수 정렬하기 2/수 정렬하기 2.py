import sys

n=int(sys.stdin.readline())
l=[]
for i in range(n): #입력
    num=int(sys.stdin.readline())
    l.append(num)

l.sort()
for i in range(n): #출력
    print(l[i])
