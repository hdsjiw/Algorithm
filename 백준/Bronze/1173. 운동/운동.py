import sys
input = sys.stdin.readline

N, m, M, T, R = map(int, input().split())

# 애초에 1분도 운동 못 하는 경우
if m + T > M:
    print(-1)
    exit()

X = m      # 현재 맥박
time = 0   # 총 경과 시간
n_time = 0 # 실제로 운동한 시간

while n_time < N:
    if X + T <= M: # 운동 가능
        X += T
        n_time += 1
    else: # 휴식
        X -= R
        if X < m:
            X = m
    time += 1

print(time)
