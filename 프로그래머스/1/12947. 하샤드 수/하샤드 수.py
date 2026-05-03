def solution(x):
    # x를 각 자리수 숫자로 분리
    digits = list(map(int, str(x)))
    # 각 자리수 숫자 합 구하기
    sum_num=sum(digits)
    # 그걸로 나눠 떨어지면 하셔드 수(True 반환)
    return x % sum_num == 0
