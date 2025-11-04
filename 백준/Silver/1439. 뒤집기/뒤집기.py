import sys

S=sys.stdin.readline().strip()
S=list(S)

n=0 # n : 최소 횟수
num0=num1=0 # 각각 덩어리 0, 1 횟수

# 첫 문자 기준
if S[0] == '0':
    num0 += 1
else:
    num1 += 1

# 덩어리 세기
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        if S[i] == '0':
            num0 += 1
        else:
            num1 += 1

print(min(num0, num1))
