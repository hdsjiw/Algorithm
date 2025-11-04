import sys

straight=False
list=[]

# 세 값 입력받기
for _ in range(3):
    x,y=map(int, sys.stdin.readline().split())
    list.append([x,y])

# points = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

# 직선인지 판별 (x2−x1)⋅(y3−y1)−(y2−y1)⋅(x3−x1)== 0
# CCW 알고리즘
if (list[1][0]-list[0][0]) * (list[2][1]-list[0][1]) - (list[1][1]-list[0][1]) * (list[2][0]-list[0][0]) == 0:
    print('WHERE IS MY CHICKEN?')
else:
    print('WINNER WINNER CHICKEN DINNER!')
