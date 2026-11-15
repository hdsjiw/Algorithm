def solution(n, m, section):
    answer = 0
    end = 0

    for s in section:
        if s > end:
            answer += 1
            end = s + m - 1

    return answer
