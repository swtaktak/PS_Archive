import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    a = [tuple(map(int, input().split())) for _ in range(n)]
    a.sort()  # 서류 점수 오름차순

    cnt = 0
    min_inter = 10**9  # 지금까지 본 면접 점수 최솟값
    for paper, inter in a:
        if inter < min_inter:
            cnt += 1
            min_inter = inter
    print(cnt)
