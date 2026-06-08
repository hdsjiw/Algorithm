n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
arr=[] #t로 시작하는 단어 배열
for word in str:
    if word.startswith(t):
        arr.append(word)
arr.sort()
print(arr[k-1])