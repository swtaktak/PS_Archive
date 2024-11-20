import sys
input = sys.stdin.readline

N = int(input())
# 가장 최소와 마주보는 애들을 찾아야 한다.
dice_list = list(map(int, input().split()))
min_idx = dice_list.index(min(dice_list))

# 최솟값 3개를 빼야 한다.
def cands(min_idx, d):
    if min_idx in [0, 5]:
        first = d[min_idx]
        # 미 평행
        not_par = [d[1], d[2], d[3], d[4]]
        # 또 미평행을 골라야 함
        second = min(not_par)
        second_idx = not_par.index(min(not_par))
        if second_idx in [0, 3]:
            third = min(d[2], d[3])
        elif second_idx in [1, 2]:
            third = min(d[1], d[4])
        return [first, second, third]
    
    elif min_idx in [1, 4]:
        first = d[min_idx]
        # 미 평행
        not_par = [d[0], d[2], d[3], d[5]]
        # 또 미평행을 골라야 함
        second = min(not_par)
        second_idx = not_par.index(min(not_par))
        if second_idx in [0, 3]:
            third = min(d[2], d[3])
        elif second_idx in [1, 2]:
            third = min(d[0], d[5])
        return [first, second, third]
    
    elif min_idx in [2, 3]:
        first = d[min_idx]
        # 미 평행
        not_par = [d[0], d[1], d[4], d[5]]
        # 또 미평행을 골라야 함
        second = min(not_par)
        second_idx = not_par.index(min(not_par))
        if second_idx in [0, 3]:
            third = min(d[1], d[4])
        elif second_idx in [1, 2]:
            third = min(d[0], d[5])
        return [first, second, third]
show_list = cands(min_idx, dice_list)

if N >= 2:
    answer = 0
    answer += 4 * sum(show_list) # 맨 꼭대기층 구석
    answer += 4 * (show_list[0] + show_list[1]) # 맨 아래 층 구석
    answer += 12 * (N-2) * show_list[0] # 맨 아래층 포함한 변(최저값)
    answer += 8 * (N-2) * show_list[1] # 변 부분 나머지, 바닥은 제외
    answer += 5 * (N-2) * (N-2) * show_list[0]  # 나머지 면 부분(5개)
else:
    dice_list.sort()
    answer = sum(dice_list[:-1])
print(answer)