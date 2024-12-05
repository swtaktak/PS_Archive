def fn(N):
    cur_sum = 0
    while N > 0:
        cur_sum += (N % 10) ** 2
        N = N // 10
    return cur_sum

N = int(input())
# 범위에 의해 최악 케이스는 729까지임.
visited = [False] * 730

while True:
    cur_num = fn(N)
    if not visited[cur_num]:
        visited[cur_num] = True
        N = cur_num
    elif cur_num == 1:
        print('HAPPY')
        break
    else:
        print('UNHAPPY')
        break