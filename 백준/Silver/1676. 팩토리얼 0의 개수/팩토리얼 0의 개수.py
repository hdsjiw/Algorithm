import math
n=int(input())
n_fac=math.factorial(n)
divide=10
val=0
while True:
    if n_fac%divide!=0:
        break
    val+=1
    divide*=10
print(val)