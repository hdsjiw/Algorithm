import sys

n,k=map(int, sys.stdin.readline().split())
tall=list(map(int, sys.stdin.readline().split()))
subTall=[]
cost=0
for i in range(len(tall)-1):
    sub=tall[i+1]-tall[i]
    subTall.append(sub)

subTall.sort()

for i in range((n-1)-(k-1)):
    cost+=subTall[i]
print(cost)