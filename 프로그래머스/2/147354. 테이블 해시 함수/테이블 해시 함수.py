from functools import reduce

def solution(data, col, row_begin, row_end):  
    # 1. 정렬
    sorted_data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    s = []
    
    # 2. S_i 계산
    for i in range(row_begin-1, row_end):
        row_sum = 0
        for val in sorted_data[i]:
            row_sum += val % (i + 1)
        s.append(row_sum)
    # 3. XOR 누적
    answer = reduce(lambda x, y: x ^ y, s)
    
    return answer