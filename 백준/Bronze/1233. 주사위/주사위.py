import sys

s1,s2,s3=map(int, sys.stdin.readline().split())
# 경우의 수 81 = 3**4
li = [0]*81

#s1, s2, s3 주사위의 모든 경우의 수를 li 리스트에 넣어줍니다.
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            
            # 인덱스 값에 1씩을 더해주고, 자연스럽게 인덱스가 같은게 많으면, 값이 커집니다.
            li[i+j+k] += 1

# li 리스트의 인덱스중 가장 많이 나온 것을 출력해줍니다.
print(li.index(max(li)))
