import sys,math

input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
else:
    scores = [int(input()) for _ in range(n)]
    scores.sort()

    # 절사 개수 (15%)
    cut = int(n * 0.15 + 0.5)

    # 절사 적용
    scores = scores[cut:n - cut] if cut > 0 else scores

    # 평균 구하기 (일반 반올림)
    avg = sum(scores) / len(scores)
    print(math.floor(avg + 0.5))
