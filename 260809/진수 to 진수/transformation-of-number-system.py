a, b = map(int, input().split())
n = input().strip()

num = int(n, a)

answer = ""

while num > 0:
    answer += str(num % b)
    num //= b

print(answer[::-1])