import sys
input = sys.stdin.readline

N, cutline = map(int, input().split())

num_list = list(map(int, input().split()))

start = 0
end = 0
odd_cnt = 0
cur_even_cnt = 0
max_even_cnt = 0

while end < N:
    # 만일 현 상태에서 홀수가 더 없어도 된다면
    if odd_cnt <= cutline:
        if num_list[end] % 2 == 0:
            cur_even_cnt += 1
            if cur_even_cnt > max_even_cnt:
                max_even_cnt = cur_even_cnt
        else:
            odd_cnt += 1
        end += 1
    else:
        if num_list[start] % 2 == 0:
            cur_even_cnt -= 1
        else:
            odd_cnt -= 1
        start += 1

print(max_even_cnt)
                