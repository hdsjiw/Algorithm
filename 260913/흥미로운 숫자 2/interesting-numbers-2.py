X, Y = map(int, input().split())

answer = 0

for num in range(X, Y + 1):
    s = str(num)

    count = {}

    for digit in s:
        count[digit] = count.get(digit, 0) + 1

    # 숫자가 정확히 2종류여야 함
    if len(count) == 2:
        values = list(count.values())

        # 한 숫자는 1번, 다른 숫자는 나머지 자리만큼 등장
        if 1 in values:
            answer += 1

print(answer)