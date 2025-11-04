import sys

n=m=0 # 인덱스 위치
max_num=0

for i in range(9):
    nums=list(map(int, sys.stdin.readline().split()))
    for j in range(9):
        if nums[j] >= max_num:
            max_num = nums[j]
            n = i + 1
            m = j + 1

print(max_num)
print(n,m)
