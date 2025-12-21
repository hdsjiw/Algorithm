import sys
input = sys.stdin.readline

S = int(input())
sum_num = 0
n = 0

i = 1
while sum_num + i <= S:
    sum_num += i
    n += 1
    i += 1

print(n)
