import math
n,k= map(int, input().split())

answer=1
for i in range(k):
    answer=answer*(n-i)

answer=answer/math.factorial(k)

print(int(answer))