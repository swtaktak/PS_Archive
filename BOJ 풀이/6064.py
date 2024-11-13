import sys
input = sys.stdin.readline
def get_lcm(a, b):
    new_a, new_b = a, b
    while new_b:
        new_a, new_b = new_b, new_a % new_b
    return a * b // new_a

t_case = int(input())
for _ in range(t_case):
    m, n, x, y = map(int, input().split())
    MAX_LIMIT = get_lcm(m, n)
    answer = -1
    if m > n:
        cur_cnt = x
    else:
        cur_cnt = y
    while cur_cnt <= MAX_LIMIT:
        if m > n:
            if (cur_cnt - y) % n == 0:
                answer = cur_cnt
                break
            else:
                cur_cnt += m
        else:
            if (cur_cnt - x) % m == 0:
                answer = cur_cnt
                break
            else:
                cur_cnt += n
    print(answer)
    