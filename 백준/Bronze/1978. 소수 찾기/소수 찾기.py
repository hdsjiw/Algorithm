import sys

n=int(sys.stdin.readline())
list=list(map(int, sys.stdin.readline().split()))
count=0

for num in list:
    for i in range(2, num+1):
        if num % i == 0:
            if num == i:
                count += 1
            break

print(count)