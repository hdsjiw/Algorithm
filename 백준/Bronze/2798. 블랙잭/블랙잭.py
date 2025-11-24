import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
nums=list(map(int, sys.stdin.readline().split()))
nums_com=list(combinations(nums, 3))
answer=0

# 조합 찾기
for i in range(len(nums_com)):
    tem=sum(nums_com[i])
    if tem>answer and tem<=m:
        answer=tem

print(answer)