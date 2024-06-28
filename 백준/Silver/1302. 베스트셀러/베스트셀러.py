def best_seller(book_list):
    keys=set(book_list)
    count=dict.fromkeys(keys,0)
    max_list=[]
    
    for i in book_list:
        count[i]+=1

        
    # 최빈값 찾기
    max_freq = max(count.values())
    modes = [k for k, v in count.items() if v == max_freq]
    
    if len(modes) > 1:
        return sorted(modes)[0]  # 최빈값이 여러 개일 때 사전 순 제일 앞 제목
    else:
        return modes[0]

n=int(input())
book_list=[]
for i in range(n):
    title=input()
    book_list.append(title)
print(best_seller(book_list))
