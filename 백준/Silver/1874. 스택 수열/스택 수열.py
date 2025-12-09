import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
current = 1  # 1부터 push할 숫자

for _ in range(n):
    num = int(input())

    # 목표 수(num)에 도달할 때까지 push
    while current <= num:
        stack.append(current)
        result.append("+")
        current += 1

    # 스택 top이 num과 같으면 pop
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        # 불가능한 경우
        print("NO")
        exit()

# 가능한 경우
print("\n".join(result))
