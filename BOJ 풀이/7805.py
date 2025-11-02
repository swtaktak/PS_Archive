import sys
input = sys.stdin.readline
def cycle_check(i):
    cur_ans = 0
    cur_pos = i
    # 현재 위치의 문자가 동일한지
    # 아니면 현재 위치의 문자가 가라키는 문자를 본다.
    # 그렇게 돌고 돌아, 반복하면 cycle
    # cycle 길이 - 1
    while True:
        if not visited[cur_pos]:
            visited[cur_pos] = True
            cur_pos = sorted_s.index(cur_s[cur_pos])
            cur_ans += 1
        else:
            break
    return cur_ans - 1

while True:
    try:
        cur_s = str(input().rstrip())
        if not cur_s:
            break
        cur_len = len(cur_s)
        sorted_s = sorted(cur_s)
        visited = [False for _ in range(len(cur_s))]
        ans = 0
        for i in range(cur_len):
            if not visited[i]:
                cur_cycle = cycle_check(i)
                ans += cur_cycle
        print(ans)
    except EOFError:
        break