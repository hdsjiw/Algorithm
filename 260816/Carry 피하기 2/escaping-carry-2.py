n = int(input())
arr = [int(input()) for _ in range(n)]

answer = -1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a = arr[i]
            b = arr[j]
            c = arr[k]

            possible = True

            while a > 0 or b > 0 or c > 0:
                if a % 10 + b % 10 + c % 10 >= 10:
                    possible = False
                    break

                a //= 10
                b //= 10
                c //= 10

            if possible:
                answer = max(answer, arr[i] + arr[j] + arr[k])

print(answer)