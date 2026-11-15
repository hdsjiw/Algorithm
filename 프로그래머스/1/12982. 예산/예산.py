def solution(d, budget):
    d.sort()
    count = 0

    for money in d:
        if budget < money:
            break

        budget -= money
        count += 1

    return count
