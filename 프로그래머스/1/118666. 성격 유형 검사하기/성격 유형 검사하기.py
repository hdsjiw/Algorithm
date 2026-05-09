def solution(survey, choices):
    category={"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    score=[0,3,2,1,0,1,2,3]
    for i in range(len(survey)):
        answer=list(survey[i])
        if choices[i]<=3:
            tem=answer[0]
        else:
            tem=answer[1]
        category[tem]+=score[choices[i]]
                   
    pairs = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    result = ""

    for left, right in pairs:
        if category[left] >= category[right]:
            result += left
        else:
            result += right
    return result