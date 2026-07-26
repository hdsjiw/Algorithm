a, b = map(int, input().split())
c, d = map(int, input().split())

overlap = max(0, min(b, d) - max(a, c))
answer = (b - a) + (d - c) - overlap

print(answer)