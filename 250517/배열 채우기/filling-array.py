integers=list(map(int,input().split()))
prints=[]
for integer in integers:
    if integer==0:
        break
    else:
        prints.append(integer)

#역순 출력
for i in range(len(prints)-1,-1,-1):
    print(prints[i],end=" ")
