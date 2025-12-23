# 1201
import sys
input = sys.stdin.readline

# idea : sum of partition
N, inc, dec = map(int, input().split())
# x1 + x2 + ... x(inc) = N인데 x1 = dec, 나머지는 dec 이하여야 한다.
min_sum = dec + (inc - 1)
max_sum = dec * inc

if N < min_sum or N > max_sum:
    print(-1)
else:
    # 해집합을 만든다.
    ans_list = [1 for _ in range(inc)]
    cur_sum = inc
    
    for i in range(inc):
        if i == 0:
            ans_list[i] += (dec - 1)
            cur_sum += (dec - 1)

        else:
            if N - cur_sum >= dec - 1:
                ans_list[i] += (dec - 1)
                cur_sum += (dec - 1)
            else:
                ans_list[i] += (N - cur_sum)
                cur_sum += (N - cur_sum)

        if cur_sum == N:
            break
        
    # ans_list를 기준으로 출력한다.
    cur_sum = 0
    prev = 0
    for a in  ans_list:
        cur_sum += a
        for i in range(cur_sum, prev, -1):
            print(i, end = " ")
        prev = cur_sum