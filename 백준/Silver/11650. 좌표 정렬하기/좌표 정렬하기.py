import sys

n=int(sys.stdin.readline().strip())
coordinate=[]

for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    coordinate.append([x,y])

sorted_coordinate = sorted(coordinate, key= lambda x : [x[0], x[1]])

for x,y in sorted_coordinate: # 출력 코드
    print(x,y)
