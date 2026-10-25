def solution(message, spoiler_ranges):
    n = len(message)
    spoiler = [-1] * n

    # 각 문자가 속한 스포 방지 구간 번호 기록
    for idx, (start, end) in enumerate(spoiler_ranges):
        for i in range(start, end + 1):
            spoiler[i] = idx

    seen = set()
    hidden_words = []

    # 메시지를 단어 단위로 순회
    pos = 0

    while pos < n:
        if message[pos] == ' ':
            pos += 1
            continue

        start = pos

        while pos < n and message[pos] != ' ':
            pos += 1

        word = message[start:pos]

        # 해당 단어가 완전히 공개되는 구간 번호
        reveal = max(spoiler[start:pos])

        if reveal == -1:
            # 스포 방지가 적용되지 않은 단어
            seen.add(word)
        else:
            # (공개 시점, 단어 시작 위치, 단어)
            hidden_words.append((reveal, start, word))

    # 공개 순서 → 같은 시점이면 왼쪽부터
    hidden_words.sort()

    answer = 0

    for _, _, word in hidden_words:
        if word not in seen:
            answer += 1

        # 중요한 단어가 아니더라도 공개된 단어로 기록
        seen.add(word)

    return answer