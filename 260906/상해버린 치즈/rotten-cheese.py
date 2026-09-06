N, M, D, S = map(int, input().split())

eat = []

for _ in range(D):
    p, m, t = map(int, input().split())
    eat.append((p, m, t))

sick = []

for _ in range(S):
    p, t = map(int, input().split())
    sick.append((p, t))

answer = 0

# 각 치즈를 상한 치즈라고 가정
for cheese in range(1, M + 1):
    possible = True

    # 실제로 아픈 사람 모두가
    # 해당 치즈를 아프기 전에 먹었는지 확인
    for sick_person, sick_time in sick:
        ate_before = False

        for p, m, t in eat:
            if (
                p == sick_person
                and m == cheese
                and t < sick_time
            ):
                ate_before = True
                break

        if not ate_before:
            possible = False
            break

    # 상한 치즈 후보가 아니라면 넘어감
    if not possible:
        continue

    # 이 치즈를 먹은 사람 수 계산
    people = set()

    for p, m, t in eat:
        if m == cheese:
            people.add(p)

    answer = max(answer, len(people))

print(answer)