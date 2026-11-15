def solution(a, b, n):
    answer = 0

    while n >= a:
        cola = (n // a) * b
        n = (n % a) + cola
        answer += cola

    return answer
