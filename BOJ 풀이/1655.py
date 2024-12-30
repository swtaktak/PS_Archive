import sys
input = sys.stdin.readline
N = int(input())

def list_put(num, cur_len):
    if len(cur_list) == 0:
        cur_list.append(num)
    else:
        start = 0
        end = cur_len
        # index 찾기
        while start < end:
            mid = (start + end) // 2
            if cur_num > cur_list[mid]:
                start = mid + 1
            else:
                end = mid
        cur_list.insert(end, cur_num)
    print(cur_list[cur_len//2])
cur_list = []
for i in range(N):
    cur_num = int(input())
    list_put(cur_num, i)