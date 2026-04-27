def solution(s):
    s = s[2:-2].split("},{")  # "{{}}" 제거 후 나누기    
    arr = [list(map(int, x.split(","))) for x in s]    
    arr.sort(key=len)
    answer = []
    
    for group in arr:
        for num in group:
            if num not in answer:
                answer.append(num)
    
    return answer