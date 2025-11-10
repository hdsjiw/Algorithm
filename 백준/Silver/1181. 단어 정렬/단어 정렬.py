import sys

n=int(sys.stdin.readline())
words=set() # 중복 방지를 위한 set 선언

for _ in range(n):
    word=sys.stdin.readline().strip()
    words.add(word)

sorted_words = sorted(words, key= lambda x : (len(x), x))

for word in sorted_words:
    print(word)
