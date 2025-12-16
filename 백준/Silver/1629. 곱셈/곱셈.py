import sys

input = sys.stdin.readline

a,b,c= map(int,input().split())

# answer : int(a**b/c)

def mul (a,b):
  if b == 1:
      return a%c
  else:
      tem = mul(a,b//2)
      if b %2 ==0:
          return (tem * tem) % c
      else:
          return (tem  * tem *a) %c
          
print(mul(a,b))
