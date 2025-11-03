import sys

m=int(sys.stdin.readline())
S=set()

for _ in range(m):
    order=sys.stdin.readline().split()
    if 'add' in order:
        if int(order[1]) not in S:
            S.add(int(order[1]))
    elif 'remove' in order:
         if int(order[1]) in S:
            S.remove(int(order[1]))
    elif 'check' in order:
         print(1 if int(order[1]) in S else 0)
    elif 'toggle' in order:
         if int(order[1]) in S:
            S.remove(int(order[1]))
         else:
            S.add(int(order[1]))
    elif 'all' in order:
        S = set(range(1, 21))
    elif 'empty' in order:
        S.clear()
