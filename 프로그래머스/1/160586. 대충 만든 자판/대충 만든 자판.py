def solution(keymap, targets):
    answer = []
    for target in targets:
        press = 0
        for char in target:
            min_val = float('inf')
            for key in keymap:
                if char in key:
                    count = key.index(char) + 1
                    min_val = min(min_val, count)
            if min_val == float('inf'):
                press = -1
                break

            press += min_val

        answer.append(press)

    return answer