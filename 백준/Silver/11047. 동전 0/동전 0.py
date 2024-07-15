n,k=map(int,input().split())
coins=[]
for i in range(n):
    coin_price=int(input())
    coins.append(coin_price)
coins.sort(reverse=True)
num=0
for coin in coins:
    if k>=coin:
        num+=(k//coin)
        k=k%coin
    else:
        pass
    
    if k<=0:
        break

print(num)
