n = int(input())
x = []
dir = []

for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

visited = {}
pos = 0

for i in range(n):
    if dir[i] == 'R':
        for j in range(pos, pos + x[i]):
            visited[j] = visited.get(j, 0) + 1

        pos += x[i]

    else:
        for j in range(pos - x[i], pos):
            visited[j] = visited.get(j, 0) + 1

        pos -= x[i]

answer = 0

for count in visited.values():
    if count >= 2:
        answer += 1

print(answer)