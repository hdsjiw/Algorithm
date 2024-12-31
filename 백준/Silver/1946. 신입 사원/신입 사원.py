import sys

t=int(sys.stdin.readline())

for _ in range(t):
    n=int(sys.stdin.readline())
    l=[]

    for _ in range(n):
        grade=list(map(int,sys.stdin.readline().split()))
        l.append(grade)

    # 서류 점수로 정렬
    l.sort(key=lambda x: x[0])
    count=0

     # 면접 점수를 기준으로 채용 가능 여부 확인
    min_grade = float('inf')  # 초기값으로 무한대 설정
    count = 0

    for _, grade2 in l:
        # 면접 점수가 현재 최소값보다 작으면 채용 가능
        if grade2 < min_grade:
            count += 1
            min_grade = grade2  # 최소값 갱신

    print(count)  
    