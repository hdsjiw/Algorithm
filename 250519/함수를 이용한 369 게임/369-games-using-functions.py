a, b = map(int, input().split())
num=0

# Please write your code here.
def magic_num(n):
    return n%3==0 or contain_num(n)

def contain_num(n):
    # 한 자리 숫자이면 3, 6, 9 중 하나인지 체크
    if n < 10:
        return n in [3, 6, 9]
    # 마지막 자리수 확인 및 나머지 자리수에 대해 재귀적으로 확인
    return (n % 10 in [3, 6, 9]) or contain_num(n // 10)



for i in range(a,b+1):
    if magic_num(i):
        num+=1
print(num)