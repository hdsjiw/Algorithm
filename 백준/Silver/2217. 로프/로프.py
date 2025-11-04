import sys

n=int(sys.stdin.readline())
list=[]

for _ in range(n):
    weight=int(sys.stdin.readline())
    list.append(weight)
# ropes = [int(sys.stdin.readline()) for _ in range(n)]

# 로프들을 내림차순 정렬
# 가장 강한 로프부터 하나씩 늘려가며, 현재 로프의 하중 * 사용 개수 의 최대값을 갱신
list.sort(reverse=True)
max_weight=0

for i in range(n):
    weight = list[i] * (i + 1)  # i+1개의 로프 사용
    max_weight = max(max_weight, weight)

print(max_weight)
