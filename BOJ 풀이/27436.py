# 방 하나는 6, 방 두개는 12추가, 방 3개는 18 추가.
# 방 N개를 지나가면, 1 + 3*N(N+1)
# 초항 포함에 주의한다.


import sys
input = sys.stdin.readline
N = int(input())
start = 0
end = N // 6 + 1 # 6방향이므로, 최대 상한은 대충 이렇게 잡아도 됨
ans = 1e19
while start <= end:
    mid = (start + end) // 2
    cutline = 1 + 3 * (mid) * (mid + 1)
    
    if cutline < N:
        start = mid + 1
    else:
        end = mid - 1
        if mid < ans:
            ans = mid
print(ans + 1)