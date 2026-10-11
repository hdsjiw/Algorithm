
from itertools import product

def solution(users, emoticons):
    answer = [0, 0]

    for discounts in product([10, 20, 30, 40], repeat=len(emoticons)):
        subscribers = 0
        revenue = 0

        for min_discount, limit in users:
            total = 0

            for price, discount in zip(emoticons, discounts):
                if discount >= min_discount:
                    total += price * (100 - discount) // 100

            if total >= limit:
                subscribers += 1
            else:
                revenue += total

        if subscribers > answer[0]:
            answer = [subscribers, revenue]
        elif subscribers == answer[0] and revenue > answer[1]:
            answer = [subscribers, revenue]

    return answer
