n, m = map(int, input().split())

# A의 움직임
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# B의 움직임
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# A의 매 시간 위치 기록
a_pos = []
pos = 0

for i in range(n):
    for _ in range(t[i]):
        pos += v[i]
        a_pos.append(pos)

# B의 매 시간 위치 기록
b_pos = []
pos = 0

for i in range(m):
    for _ in range(t2[i]):
        pos += v2[i]
        b_pos.append(pos)

answer = 0
leader = 0
# 0: 아직 선두 없음 또는 동점만 있었음
# 1: A가 선두
# 2: B가 선두

for i in range(len(a_pos)):
    if a_pos[i] > b_pos[i]:
        current = 1
    elif a_pos[i] < b_pos[i]:
        current = 2
    else:
        # 공동 선두면 선두가 바뀐 것으로 보지 않음
        continue

    if leader == 0:
        leader = current
    elif leader != current:
        answer += 1
        leader = current

print(answer)