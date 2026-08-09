a, b = map(int, input().split())

# Please write your code here.
answer = 0

for n in range(a, b + 1):
    # 1. 소수 판별
    is_prime = True

    if n < 2:
        is_prime = False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break

    # 2. 소수이면서 자리수 합이 짝수인지 확인
    if is_prime:
        digit_sum = sum(map(int, str(n)))

        if digit_sum % 2 == 0:
            answer += 1

print(answer)