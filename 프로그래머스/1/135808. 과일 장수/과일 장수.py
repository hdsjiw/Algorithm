def solution(k, m, score):
    score.sort(reverse=True) # 정렬
    result = [score[i:i+m] for i in range(0, len(score), m)] # m개씩 자르기
    money=0
    for i in range(len(result)):
        if len(result[i])==m: # 해당 상자에 사과 개수 알맞게
            money+=min(result[i])*m
    return money