import sys
input = sys.stdin.readline

N = int(input())
ans = 0
stack = [] 

for _ in range(N):
    cur = int(input())
    cnt = 1

    # 나보다 키가 작은 사람은 모두 정산해서 반영하자.
    # 주의 a < b < c 면 a - c는 안보임. 이거에 매우 주의!
    while stack and stack[-1][0] < cur:
        ans += stack[-1][1]
        stack.pop()

    # 같은 키 누적해서 가져옴
    if stack and stack[-1][0] == cur:
        ans += stack[-1][1]
        cnt += stack[-1][1]
        stack.pop()

    # 내 앞에 큰 키가 있으면 그 사람하고 나도 보여야함.
    if stack:
        ans += 1

    # 현재 사람을 "묶음"으로 한 번만 push
    stack.append((cur, cnt))

print(ans)
