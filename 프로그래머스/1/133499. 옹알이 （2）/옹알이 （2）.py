def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        i = 0
        prev = ""

        while i < len(b):
            for word in words:
                if b.startswith(word, i) and word != prev:
                    i += len(word)
                    prev = word
                    break
            else:
                break

        if i == len(b):
            answer += 1

    return answer