import sys
input = sys.stdin.readline

name = input().strip()
names = [0] * 26

for ch in name:
    names[ord(ch) - 65] += 1

odd = 0
mid = ""
left = ""

for i in range(26):
    if names[i] % 2 == 1:
        odd += 1
        mid = chr(i + 65)
    left += chr(i + 65) * (names[i] // 2)

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(left + mid + left[::-1])
