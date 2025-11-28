import sys
input = sys.stdin.readline

# 방향: 동(0), 남(1), 서(2), 북(3)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

case = 1

while True:
    n, m, r = map(int, input().split())
    if (n, m, r) == (0, 0, 0):
        break

    rocks = set()
    
    # rock 입력
    cur = 0
    while cur < r:
        line = list(map(int, input().split()))
        for i in range(0, len(line), 2):
            c, rr = line[i], line[i+1]
            # 좌표 뒤집기 (입력은 (col,row), row는 위가 1)
            rocks.add((m - rr, c - 1))
            cur += 1

    # 시작점
    c, rr = map(int, input().split())
    cur_r, cur_c = m - rr, c - 1

    # 초기 방향 결정
    if c == 1:
        d = 0   # 동
    elif c == n:
        d = 2   # 서
    elif rr == 1:
        d = 1   # 남
    else:
        d = 3   # 북

    visited = 1  # 시작 칸 포함

    # 시뮬레이션
    while True:
        nr = cur_r + dr[d]
        nc = cur_c + dc[d]

        # 밖이면 끝
        if not (0 <= nr < m and 0 <= nc < n):
            break

        # 앞이 돌인가?
        if (nr, nc) not in rocks:
            cur_r, cur_c = nr, nc
            visited += 1
        else:
            # 오른쪽
            right = (d + 1) % 4
            rr2 = cur_r + dr[right]
            rc2 = cur_c + dc[right]

            if 0 <= rr2 < m and 0 <= rc2 < n and (rr2, rc2) not in rocks:
                d = right
                visited += 1
                cur_r, cur_c = rr2, rc2
                continue

            # 왼쪽
            left = (d + 3) % 4
            lr2 = cur_r + dr[left]
            lc2 = cur_c + dc[left]

            if 0 <= lr2 < m and 0 <= lc2 < n and (lr2, lc2) not in rocks:
                d = left
                visited += 1
                cur_r, cur_c = lr2, lc2
                continue

            # 뒤
            d = (d + 2) % 4

    print(f"Case {case}: {cur_c+1} {m-cur_r} {visited}")
    case += 1