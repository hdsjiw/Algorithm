import sys

score_sum=0

for _ in range(5):
    score=int(sys.stdin.readline())
    score_sum+=score

print(score_sum)
