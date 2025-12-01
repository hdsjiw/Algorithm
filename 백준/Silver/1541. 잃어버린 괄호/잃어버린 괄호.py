import sys

input=sys.stdin.readline

n = str(input())
m = n.split('-')

answer = 0
#  -로 시작할 경우
x = sum(map(int, (m[0].split('+'))))
if n[0] == '-':
    answer -= x
else:
    answer += x

for x in m[1:]: # 1번째 작업 이미 진행
    x = sum(map(int, (x.split('+'))))
    answer -= x
print(answer)
