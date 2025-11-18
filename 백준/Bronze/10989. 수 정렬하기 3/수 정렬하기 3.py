import sys

n = int(sys.stdin.readline().strip())
counts = [0] * 10001   # 숫자의 범위가 1~10000인 경우

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    counts[num] += 1

for num in range(1, 10001):
    for _ in range(counts[num]):
        print(num)
