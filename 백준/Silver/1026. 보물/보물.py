n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=0

a.sort()
for i in range(len(a)):
    # a 재배열->b에서 가장 큰 값에 가장 작은 수 매칭
    # 가장 큰 수를 pop 해주자
    s+=a[i]*max(b)
    index=b.index(max(b))
    b.pop(index)

print(s)