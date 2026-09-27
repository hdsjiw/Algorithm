def solution(cards):
    visited = [False] * len(cards)
    group_sizes = []

    for start in range(len(cards)):
        if visited[start]:
            continue

        current = start
        size = 0

        while not visited[current]:
            visited[current] = True
            size += 1
            current = cards[current] - 1  # 카드 번호를 배열 인덱스로 변환

        group_sizes.append(size)

    if len(group_sizes) < 2:
        return 0

    group_sizes.sort(reverse=True)
    return group_sizes[0] * group_sizes[1]