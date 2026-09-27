def solution(k, ranges):
    prefix = [0.0]  # prefix[i]: x=0부터 x=i까지의 넓이

    while k != 1:
        next_k = k // 2 if k % 2 == 0 else 3 * k + 1
        prefix.append(prefix[-1] + (k + next_k) / 2)
        k = next_k

    n = len(prefix) - 1
    answer = []

    for a, b in ranges:
        end = n + b  # 음수 b는 끝점에서 거꾸로 센 위치

        if a > end:
            answer.append(-1.0)
        else:
            answer.append(prefix[end] - prefix[a])

    return answer