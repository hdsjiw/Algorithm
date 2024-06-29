n = int(input())
l = []

# 다각형의 꼭지점 좌표를 리스트에 저장
for i in range(n):
    x, y = map(int, input().split())
    l.append([x, y])
l.append([l[0][0],l[0][1]])
as1 = as2 = 0

# 신발끈 공식(Shoelace Formula)을 사용하여 다각형의 넓이 계산
for i in range(n):
    as1 += l[i][0] * l[i+1][1]
    as2 += l[i][1] * l[i+1][0]  

area = abs(as1 - as2) / 2

print(f"{area:.1f}")