ability = list(map(int, input().split()))

ans = float('inf')

# 1팀: i, j
for i in range(6):
    for j in range(i + 1, 6):

        # 1팀에 속하지 않은 사람들
        remain1 = []
        for x in range(6):
            if x != i and x != j:
                remain1.append(x)

        # 남은 4명 중 2명을 2팀으로 선택
        for a in range(4):
            for b in range(a + 1, 4):
                k = remain1[a]
                l = remain1[b]

                # 나머지 2명은 자동으로 3팀
                remain2 = []
                for x in remain1:
                    if x != k and x != l:
                        remain2.append(x)

                m, n = remain2

                team1 = ability[i] + ability[j]
                team2 = ability[k] + ability[l]
                team3 = ability[m] + ability[n]

                max_team = max(team1, team2, team3)
                min_team = min(team1, team2, team3)

                ans = min(ans, max_team - min_team)

print(ans)