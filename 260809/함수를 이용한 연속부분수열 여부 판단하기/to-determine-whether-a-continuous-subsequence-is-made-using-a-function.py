n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = "No"

for i in range(n1 - n2 + 1):
    if a[i:i + n2] == b:
        answer = "Yes"
        break

print(answer)
