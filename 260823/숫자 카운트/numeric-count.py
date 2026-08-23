n = int(input())

a, b, c = [], [], []

for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

ans = 0

for x in range(1, 10):
    for y in range(1, 10):
        for z in range(1, 10):

            # 세 숫자는 서로 달라야 함
            if x == y or y == z or x == z:
                continue

            candidate = [x, y, z]
            possible = True

            for i in range(n):
                num = str(a[i])
                guess = [int(num[0]), int(num[1]), int(num[2])]

                cnt1 = 0
                cnt2 = 0

                for j in range(3):
                    if candidate[j] == guess[j]:
                        cnt1 += 1
                    elif candidate[j] in guess:
                        cnt2 += 1

                if cnt1 != b[i] or cnt2 != c[i]:
                    possible = False
                    break

            if possible:
                ans += 1

print(ans)