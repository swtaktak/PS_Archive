import sys
input = sys.stdin.readline

start, q = map(int, input().split())
salary = [0] * (10**9 + 1)
salary[0] = start
cur_r = 0

for i in range(1, 10**9+1):
    cur_r = salary[i-1] % i
    salary[i] = salary[i-1] + (i - cur_r)
print(salary)