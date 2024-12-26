n=int(input())
l=[]
for i in range(n):
    start, end = input().split()
    start = (int(start[:2]) * 60) + int(start[2:]) - 10
    end = (int(end[:2]) * 60) + int(end[2:]) + 10
    l.append([start, end])

l.sort()


rest = 0
last = 600  # 첫 회의 시작 전 기본값: 10:00 AM

for run, stop in l:
    if run > last:  # 회의 간격이 있을 때만 계산
        rest = max(rest, run - last)
    last = max(last, stop)

# 회의 끝 이후 남은 시간 계산 (마지막 회의 종료 ~ 22:00)
rest = max(rest, 1320 - last)

print(rest)
