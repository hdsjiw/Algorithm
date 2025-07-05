word = ['L', 'E', 'B', 'R', 'O','S']

charactor=input()
# 해당 문자를 찾지 못했다면 -1
idx = -1

# 문자 탐색
for i, char in enumerate(word):
    if char == charactor:
        idx = i

# 문자가 존재하지 않는 경우
if idx == -1:
    print("None")
else:
    print(idx)

