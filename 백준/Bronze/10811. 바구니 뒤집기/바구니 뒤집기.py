import sys

n,m=map(int, sys.stdin.readline().split())
list=list([i+1 for i in range(n)])

for _ in range(m):
    i,j=map(int, sys.stdin.readline().split())
    temp=list[i-1:j]
    temp.reverse()
    list[i-1:j]=temp

for num in list:
    print(num,end=" ")
