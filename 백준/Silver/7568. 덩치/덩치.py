import sys

input = sys.stdin.readline

n = int(input())
people=[]

for t in range(n):
    weight,height=map(int, input().split())
    people.append([weight,height])

# 덩치 등수 구하기
for i in range(n):
    rank = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    print(rank, end=" ")
