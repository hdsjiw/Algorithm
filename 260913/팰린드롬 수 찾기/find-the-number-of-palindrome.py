X, Y = map(int, input().split())

answer = 0

for num in range(X, Y + 1):
    s = str(num)

    if s == s[::-1]:
        answer += 1

print(answer)