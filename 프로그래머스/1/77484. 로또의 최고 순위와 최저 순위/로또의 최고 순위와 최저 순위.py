def rank(x):
        return 7 - x if x >= 2 else 6
    
def solution(lottos, win_nums):
    match = len(set(lottos) & set(win_nums)) #일치하는 숫자 개수
    unknown = lottos.count(0) #0인 숫자 개수
    return rank(match + unknown), rank(match)