def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            prev_index = stack.pop()
            answer[prev_index] = number

        stack.append(i)

    return answer

    return answer