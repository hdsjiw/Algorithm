N,M=map(int,input().split())
integers=list(map(int,input().split()))
number=0


# 문자 탐색
for num in integers:
    if num == M:
        number+=1

print(number)
