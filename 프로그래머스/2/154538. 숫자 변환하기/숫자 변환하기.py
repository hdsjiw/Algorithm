from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))  # 현재 값, 연산 횟수

    visited = set()
    visited.add(x)

    while queue:
        current, count = queue.popleft()

        if current == y:
            return count

        for next_value in (current + n, current * 2, current * 3):
            if next_value <= y and next_value not in visited:
                visited.add(next_value)
                queue.append((next_value, count + 1))

    return -1