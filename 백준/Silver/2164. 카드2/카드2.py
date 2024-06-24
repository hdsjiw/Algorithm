from collections import deque

n = int(input())
queue = deque(range(1, n + 1))

while len(queue) > 1:
    queue.popleft()           # 맨 앞의 요소 제거
    queue.append(queue.popleft())  # 다음 요소를 맨 뒤로 이동

print(queue[0])