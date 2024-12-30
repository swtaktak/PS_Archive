# 거신병 2
# 9의 최소 개수를 센 다음에, 반대로 올라가면서 9의 개수를 조절하는 방식
# 9가 남는다면, 실패 처리! 

import sys
input = sys.stdin.readline

N = int(input())
block_list = list(map(int, input().split()))
ones, nins = map(int, input().split())

block_cnt = []
for b in block_list:
    # 모두 1의 개수라고 취급한다.
    block_cnt.append([b, 0])
    
prev_sum = 0
min_nine = 0
for i in range(N):
    cur_sum = block_list[i]
    while cur_sum <= prev_sum:
        cur_sum += 8
        block_cnt[i][0] -= 1
        block_cnt[i][1] += 1
        min_nine += 1
        if block_cnt[i][0] == -1:
            print(-1)
            exit()
    prev_sum = cur_sum

if nins < min_nine:
    print(-1)
else:
    # 추가로 필요한 9를 채운다.
    add_nine = nins - min_nine
    cur_floor = N - 1
    next_sum = 999999999999
    while add_nine > 0 and cur_floor >= 0:
        # 현재 층의 1의 개수
        cur_one = block_cnt[cur_floor][0]
        cur_sum = block_cnt[cur_floor][0] + block_cnt[cur_floor][1] * 9
        while True:
            if cur_one == 0 or add_nine == 0:
                break
            else:
                if cur_sum + 8 < next_sum and add_nine > 0:
                    cur_sum += 8
                    block_cnt[cur_floor][0] -= 1
                    block_cnt[cur_floor][1] += 1
                    add_nine -= 1
                    cur_one -= 1
                else:
                    break
        next_sum = block_cnt[cur_floor][0] * 1 + block_cnt[cur_floor][1] * 9
        cur_floor -= 1
        
    if add_nine > 0:
        print(-1)
    else:
        for b in block_cnt:
            cur_list = [1] * b[0] + [9] * b[1]
            for c in cur_list:
                print(c, end = " ")
            print()