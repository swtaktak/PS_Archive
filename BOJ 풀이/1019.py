# 책 페이지 문제
# 점화식이 좀 어렵다.

N = int(input())
cnt_list = [0 for _ in range(10)]

for i in range(1, N + 1):
    str_i = str(i)
    for c in str_i:
        cnt_list[int(c)] += 1
print(cnt_list)