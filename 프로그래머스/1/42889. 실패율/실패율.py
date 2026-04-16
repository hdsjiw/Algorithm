def solution(N, stages):
    people = len(stages)
    failures = {} #실패율

    for i in range(N):
        temp = stages.count(i + 1) # 해당 스테이지에서 실패하 사람 수

        if people == 0:
            failure = 0
        else:
            failure = temp / people

        people -= temp
        failures[i + 1] = failure

    sorted_failure = sorted(failures.items(), key=lambda x: x[1], reverse=True)
    answer = [stage for stage, failure in sorted_failure]

    return answer