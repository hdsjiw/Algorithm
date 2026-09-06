n = int(input())

l = []
r = []

for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

answer = 0

for a in range(n):
    for b in range(a + 1, n):
        for c in range(b + 1, n):
            possible = True

            for i in range(n):
                if i == a or i == b or i == c:
                    continue

                for j in range(i + 1, n):
                    if j == a or j == b or j == c:
                        continue

                    # 두 선분이 겹치는 경우
                    if not (r[i] < l[j] or r[j] < l[i]):
                        possible = False
                        break

                if not possible:
                    break

            if possible:
                answer += 1

print(answer)