a = list(input().strip())
max_num = 0

for i in range(len(a)):
    tem = a[:]  # 복사

    # 한 자리 뒤집기
    if tem[i] == '0':
        tem[i] = '1'
    else:
        tem[i] = '0'

    # 이진수 → 십진수 변환
    num = 0
    for j in range(len(tem)):
        num += int(tem[j]) * (2 ** (len(tem)-1-j))

    max_num = max(max_num, num)

print(max_num)