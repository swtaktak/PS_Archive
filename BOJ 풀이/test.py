import sys
input = sys.stdin.readline

start, fail = map(int, input().split())

answer = 1

for i in range(fail):
    cur_prob = start / 100 + (0.005) * i
    answer *= (1 - cur_prob)
    
print(answer * 100)