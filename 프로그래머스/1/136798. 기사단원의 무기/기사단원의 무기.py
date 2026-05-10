import math

def count_divisors(n):
    divisors = []
    # 제곱근까지만 반복
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            # 짝이 되는 약수 추가 (중복 방지)
            if i != n // i:
                divisors.append(n // i)
    return len(divisors)

def solution(number, limit, power):
    # 각 number 들의 약수 개수 구하기->배열
    l=[]
    number=[i for i in range(1,number+1)]
    for num in number:
        tem=count_divisors(num)
        if tem>limit:   # 약수 개수가 limit 초과하면 power로 변환
            l.append(power)
        else: 
            l.append(tem)
    
    return sum(l)