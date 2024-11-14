import sys
input = sys.stdin.readline

N = int(input())
abs_min = 2000000001 # 문제 조건에 따른 최악 케이스 + 1

liquid_list = list(map(int, input().split()))
liquid_list.sort()
start = 0 # 투포인터용
end = N-1 # 투포인터용
cur_best_low = liquid_list[0] # 결과저장용
cur_best_high = liquid_list[N-1] # 결과저장용
while start < end:
    cur_mix = liquid_list[start] + liquid_list[end]
    if abs(cur_mix) < abs_min:
        abs_min = abs(cur_mix)
        cur_best_low = liquid_list[start]
        cur_best_high = liquid_list[end]
    if cur_mix < 0:
        start += 1
    else:
        end -= 1
print("%d %d" %(cur_best_low, cur_best_high))