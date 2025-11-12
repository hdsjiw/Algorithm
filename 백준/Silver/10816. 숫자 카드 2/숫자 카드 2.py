import sys,bisect

input = sys.stdin.readline

n = int(input())
cards = sorted(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    left = bisect.bisect_left(cards, t)
    right = bisect.bisect_right(cards, t)
    print(right - left, end=' ')
    