from itertools import permutations
import re


def solution(expression):
    # 숫자와 연산자를 순서대로 분리
    tokens = re.split(r'([+\-*])', expression)
    tokens = [
        int(token) if token.isdigit() else token
        for token in tokens
    ]

    operators = set(re.findall(r'[+\-*]', expression))
    answer = 0

    def calculate(left, operator, right):
        if operator == '+':
            return left + right
        if operator == '-':
            return left - right
        return left * right

    # 등장한 연산자의 모든 우선순위 확인
    for priority in permutations(operators):
        current = tokens[:]

        for operator in priority:
            next_tokens = []
            index = 0

            while index < len(current):
                if current[index] == operator:
                    left = next_tokens.pop()
                    right = current[index + 1]

                    next_tokens.append(
                        calculate(left, operator, right)
                    )
                    index += 2
                else:
                    next_tokens.append(current[index])
                    index += 1

            current = next_tokens

        answer = max(answer, abs(current[0]))

    return answer