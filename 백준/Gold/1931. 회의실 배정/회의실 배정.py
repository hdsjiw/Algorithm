import sys

n=int(sys.stdin.readline())
meetings=[]
use_end=0
max_use=0

for _ in range(n):
    start,end=map(int, sys.stdin.readline().split())
    meetings.append([start,end])

# 끝나는 시간 기준으로, 끝이 같으면 시작 빠른 순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

for start,end in meetings:
    if use_end<=start:
        use_end=end
        max_use+=1

print(max_use)
