N, B = map(int, input().split())

P = [int(input()) for _ in range(N)]

answer = 0

for i in range(N):
    prices = P[:]
    prices[i] //= 2

    prices.sort()

    total = 0
    count = 0

    for price in prices:
        if total + price <= B:
            total += price
            count += 1
        else:
            break

    answer = max(answer, count)

print(answer)