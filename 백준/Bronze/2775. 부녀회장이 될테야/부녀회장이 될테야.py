import sys

t=int(sys.stdin.readline().strip())
people=[i for i in range(14)]

for _ in range(t):
    k=int(sys.stdin.readline().strip())
    n=int(sys.stdin.readline().strip())
    f = [i for i in range(1, n+1)]  # 0층 리스트
    for i in range(k):  # 층 수 만큼 반복
        for j in range(1, n):  # 1 ~ n-1까지 (인덱스로 사용)
            f[j] += f[j-1]  # 층별 각 호실의 사람 수를 변경
    print(f[-1])  # 가장 마지막 수 출력
