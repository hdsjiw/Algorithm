n = int(input())

lines = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0

for i in range(n):
    x1, x2 = lines[i]

    for j in range(n):
        if i != j:
            y1, y2 = lines[j]

            if (x1 - y1) * (x2 - y2) < 0:
                break
    else:
        answer += 1

print(answer)