n=int(input())

connect=0
for i in range(n):
    a=int(input())
    connect+=a

print(connect-(n-1))