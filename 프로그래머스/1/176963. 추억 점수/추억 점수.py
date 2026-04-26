def solution(name, yearning, photo):
    answer=[]
    for i in range(len(photo)):
        score=0
        for j in range(len(photo[i])):
            if photo[i][j] in name: # 그리워하는 사람일 때
                idx=name.index(photo[i][j])
                score+=yearning[idx]
        answer.append(score)
    return answer