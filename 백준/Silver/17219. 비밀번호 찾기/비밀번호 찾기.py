import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_to_site = {}
num_to_pw = {}
site_to_num = {}

for i in range(1,n+1):
    site,pw=input().split()
    num_to_site[i]=site
    num_to_pw[i]=pw
    site_to_num[site]=i
for _ in range(m):
    tem=input().strip()
    num=site_to_num[tem]
    print(num_to_pw[num])
