# wilson theorem
# 반복 부분을 n+a로 분류하면 a = (n-1)/n 형태
# 이게 되는 경우는 3k+7이 소수일 때만 가능
# 즉 소수 카운팅 시간이다.
import sys
input = sys.stdin.readline

Q = int(input())
prime_list = [True] * (3*(10**6) + 8)
N = 3*(10**6) + 8
for i in range(2, int(N**0.5)+ 1):
    if prime_list[i]:
        for j in range(2*i, N, i):
            prime_list[j] = False

answer_list = [0] * (10**6 + 1)
for i in range(1, 10**6 + 1):
    cur_num = 3*i + 7
    if prime_list[cur_num]:
        answer_list[i] = answer_list[i-1] + 1
    else:
        answer_list[i] = answer_list[i-1]

for _ in range(Q):
    cur_q = int(input())
    print(answer_list[cur_q])