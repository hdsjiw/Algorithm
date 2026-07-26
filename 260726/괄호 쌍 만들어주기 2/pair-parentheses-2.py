a = input().strip()

open_count = 0
answer = 0

for i in range(1, len(a)):
    if a[i - 1] == "(" and a[i] == "(":
        open_count += 1

    elif a[i - 1] == ")" and a[i] == ")":
        answer += open_count

print(answer)