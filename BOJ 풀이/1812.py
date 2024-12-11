import sys
input = sys.stdin.readline
N = int(input()) # 홀수라서 가능함. 짝수면 못 구함
sum_list = []
total = 0
for _ in range(N):
    cur_sum = int(input())
    total += cur_sum
    sum_list.append(cur_sum)
total = total // 2
# 2, 3 / 4, 5 / .... N번꺼지의 합을 구한다.
# 1 2 / 2 3 / 3 4 / 4 5 / 5 1
not_first = 0
for i in range(1, N, 2):
    not_first += sum_list[i]

ans = []
ans.append(total - not_first)

for i in range(0, N-1):
    ans.append(sum_list[i] - ans[-1])

for a in ans:
    print(a)