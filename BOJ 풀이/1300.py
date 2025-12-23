# 1300
import sys
input = sys.stdin.readline

def count(num):
    cnt = 0
    for i in range(1, size + 1):
        # N단에 num보다 작거나 같은거 몇개인가.
        cnt += min(size, num // i)
    return cnt


size = int(input())
K = int(input()) # 작은 수부터 K번째

start = 1
end = size ** 2

while start < end:
    mid = (start + end) // 2
    cur_cnt = count(mid)

    # 개수가 딱 맞는 lower_bound를 찾는다.
    # 이렇게 하는 이유는, 판에 있는 값에서만 개수가 달라지기 때문이다.
    # lower_bound 문제기 때문에 end = mid
    if cur_cnt < K:
        start = mid + 1
    else:
        end = mid
        
print(end)