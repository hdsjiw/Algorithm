word1 = input()
word2 = input()

# Please write your code here.
# 각 단어를 알파벳 순으로 정렬해서 동일하면 yes 아니면 no
word1="".join(sorted(word1))
word2="".join(sorted(word2))

if word1==word2:
    print("Yes")
else:
    print("No")