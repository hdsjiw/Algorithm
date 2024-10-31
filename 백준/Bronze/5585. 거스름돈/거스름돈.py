money=int(input())
n=1000-money

coins = (500,100,50,10,5,1)
count = 0
for coin in coins:
    count += n//coin
    n%=coin
print(count)

