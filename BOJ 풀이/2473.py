import sys
input = sys.stdin.readline

N = int(input())
abs_min = 3000000004 # 문제 조건에 따른 최악 케이스 + 1

liquid_list = list(map(int, input().split()))
liquid_list.sort()
start = 0 # 투포인터용
end = N-1 # 투포인터용
cur_best_low = liquid_list[0] 
cur_best_mid = liquid_list[1] 
cur_best_high = liquid_list[2]

# i를  시작 커트라인으로 잡아 고정시키고 나머지를 투포인터 돌리기.
# 왜 이분 탐색 풀이가 안되는가?
for i in range(N - 2):
    cur_start = i+1
    cur_end = N-1
    while cur_start < cur_end:
        cur_mix = liquid_list[i] + liquid_list[cur_start] + liquid_list[cur_end]
        if abs(cur_mix) < abs_min:
            abs_min = abs(cur_mix)
            cur_best_low = liquid_list[i] 
            cur_best_mid = liquid_list[cur_start] 
            cur_best_high = liquid_list[cur_end]
        if cur_mix < 0:
            cur_start += 1
        else:
            cur_end -= 1
print("%d %d %d" %(cur_best_low, cur_best_mid, cur_best_high))

"""
fail code : 왜 이분 탐색이 불가능한가?

def triple_mix(start, end, liquid_list):
    cur_cand = liquid_list[start: end + 1]
    best_mix_here = 3000000004
    best_mix_list = [-1, -1, -1]
    # 용액을 3개 이상 섞을 수 있다면
    if len(cur_cand) >= 3:
        left = 0
        right = len(cur_cand)
        mid = (left + right) // 2
        while left <= right and mid != 0 and mid != len(cur_cand) - 1:
            mid = (left + right) // 2
            mix_here = cur_cand[0] + cur_cand[-1] + cur_cand[mid]
            if abs(mix_here) < best_mix_here:
                best_mix_here = mix_here
                best_mix_list = [cur_cand[0], cur_cand[mid], cur_cand[-1]]
            if mix_here < 0:
                left += 1
            else:
                right -= 1
    return [best_mix_here, best_mix_list[0], best_mix_list[1], best_mix_list[2]]


while start < end:
    cur_best_list = triple_mix(start, end, liquid_list)
    if abs(cur_best_list[0]) < abs_min:
        abs_min = abs(cur_best_list[0])
        cur_best_low = cur_best_list[1] 
        cur_best_mid = cur_best_list[2] 
        cur_best_high = cur_best_list[3]
    if cur_best_list[0] < 0:
        start += 1
    else:
        end -= 1
        
print("%d %d %d" %(cur_best_low, cur_best_mid, cur_best_high))
"""