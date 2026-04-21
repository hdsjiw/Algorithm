def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        tem=array[commands[i][0]-1:commands[i][1]]
        tem.sort()
        k=commands[i][2]
        answer.append(tem[k-1])
    return answer