import sys

n,m=map(int, sys.stdin.readline().split())
list = [i+1 for i in range(n)]

for _ in range(m): # 공 교환
    i,j=map(int, sys.stdin.readline().split())
    list[i-1],list[j-1]=list[j-1],list[i-1]

for num in list: # 출력 코드
    print(num,end=" ")