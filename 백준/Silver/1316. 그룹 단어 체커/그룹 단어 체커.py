n=int(input())
group_num=0

for i in range(n):
    a=input()
    word = [char for char in a]
    #print(word)
    emer_word=[]
    tem=""
    check=0
    for i in range(len(word)):
        if tem!=word[i]:
            emer_word.append(word[i])
        tem=word[i]
    #print(emer_word)
    for i in range(len(emer_word)):
        if emer_word.count(emer_word[i])>1:
            break
        else:
            check+=1
    if check==len(emer_word):
        group_num+=1

print(group_num)
