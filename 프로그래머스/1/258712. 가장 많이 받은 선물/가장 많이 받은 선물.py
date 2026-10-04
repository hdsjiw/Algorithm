def solution(friends, gifts):
    n = len(friends)

    # 이름 -> 인덱스
    idx = {name: i for i, name in enumerate(friends)}

    # gift_count[i][j] = i가 j에게 준 선물 수
    gift_count = [[0] * n for _ in range(n)]

    # 준 선물 수, 받은 선물 수
    give = [0] * n
    receive = [0] * n

    for gift in gifts:
        giver, receiver = gift.split()

        a = idx[giver]
        b = idx[receiver]

        gift_count[a][b] += 1
        give[a] += 1
        receive[b] += 1

    # 선물 지수 = 준 선물 - 받은 선물
    gift_score = [
        give[i] - receive[i]
        for i in range(n)
    ]

    # 다음 달 받을 선물 개수
    next_gift = [0] * n

    # 두 사람씩 비교
    for i in range(n):
        for j in range(i + 1, n):

            # i가 j에게 더 많이 줬다면
            if gift_count[i][j] > gift_count[j][i]:
                next_gift[i] += 1

            # j가 i에게 더 많이 줬다면
            elif gift_count[i][j] < gift_count[j][i]:
                next_gift[j] += 1

            # 서로 주고받은 수가 같거나 둘 다 0이라면 선물 지수 비교
            else:
                if gift_score[i] > gift_score[j]:
                    next_gift[i] += 1

                elif gift_score[i] < gift_score[j]:
                    next_gift[j] += 1

    return max(next_gift)