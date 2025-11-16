# DP 같지만..
# DP로 풀기에는 어렵지 않나..?

# 아무튼 1,000원은 매일 먹어야 하고
# 아무튼 4,000원을 더 써서 가치를 최대한 높게 만들자.

import sys
import heapq
input = sys.stdin.readline

day, money = map(int, input().split())
diff_q = []
heapq.heapify(diff_q)
ans = 0

for _ in range(day):
    five, one = map(int, input().split())
    # 차이를 더 줄 것이다.
    heapq.heappush(diff_q, one - five)
    ans += one
    money -= 1000
    
while money // 4000 > 0 and diff_q:
    money -= 4000
    cur_diff = heapq.heappop(diff_q) * -1
    if cur_diff == 0:
        money += 4000
    elif cur_diff < 0:
        break
    else:
        ans += cur_diff
print(ans)