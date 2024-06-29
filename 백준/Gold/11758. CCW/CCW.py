p1=list(map(int,input().split()))
p2=list(map(int,input().split()))
p3=list(map(int,input().split()))


ccw=(p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])
if ccw<0: # 시계 방향
    print(-1)
elif ccw>0: #반시계 방향
    print(1)
else: # m1==m2 #직선
    print(0)