import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]

def repaint_count(x, y):
    count_W = 0  # 맨 왼쪽 위가 W일 경우
    count_B = 0  # 맨 왼쪽 위가 B일 경우
    
    for i in range(8):
        for j in range(8):
            current = board[x+i][y+j]
            # (i + j) 짝수면 시작 색과 같아야 함
            if (i + j) % 2 == 0:
                if current != 'W':
                    count_W += 1
                if current != 'B':
                    count_B += 1
            else:  # 홀수면 시작 색과 반대여야 함
                if current != 'B':
                    count_W += 1
                if current != 'W':
                    count_B += 1

    return min(count_W, count_B)

result = 999999
for i in range(n - 7):
    for j in range(m - 7):
        result = min(result, repaint_count(i, j))

print(result)
