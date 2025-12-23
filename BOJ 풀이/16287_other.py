import sys
input = sys.stdin.readline

W, N = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

possible = [False] * (W + 1)

for i in range(1, N - 2):
    # 오른쪽 쌍 (i, j)로 need를 확인
    ai = A[i]
    for j in range(i + 1, N):
        s = ai + A[j]
        if s >= W:
            break
        if possible[W - s]:
            print("YES")
            sys.exit(0)

    # 왼쪽 쌍 (p, i) 누적
    for p in range(i):
        s2 = A[p] + ai
        if s2 < W:
            possible[s2] = True

print("NO")
