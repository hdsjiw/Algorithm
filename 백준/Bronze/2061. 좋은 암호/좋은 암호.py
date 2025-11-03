import sys

k,l=map(int, sys.stdin.readline().split())
good_password=True

# 소수 판별 변형
# 2~x-1까지 나눠보며 소인수분해 되는 수를 찾는다
for i in range(2, l): #효율적인 버전
    # x가 해당 수로 나누어떨어진다면 해당 수를 리스트에 추가
    if k % i == 0:
       print("BAD",i)
       good_password=False
       break

if good_password:
    print("GOOD")
    