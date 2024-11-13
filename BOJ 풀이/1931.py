import sys
input = sys.stdin.readline
tt_cnt = int(input())
m_list = []
for i in range(tt_cnt):
    start, end = map(int, input().split())
    m_list.append((start, end))

# 빨리 끝나는걸 먼저 하고, 동일하면 빨리 시작하는 순서로 정렬하기.
m_list.sort(key = lambda x : (x[1], x[0]))

end_time = 0
cnt = 0

for cur_m in m_list:
    if end_time <= cur_m[0]:
        cnt += 1
        end_time = cur_m[1]
print(cnt)