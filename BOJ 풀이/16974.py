#  분할정복 + DP
#  일단 대체 몇 장을 먹어야 하는지도 계산해야 하는 고난이도 문제
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
# 레벨-L 버거는 햄버거번, 레벨-(L-1) 버거, 패티, 레벨-(L-1)버거, 햄버거번으로 이루어져 있다.
# 즉 Patty는 2배 + 1 의 반복
len_burger = [0] * (N + 1)
patty_cnt = [0] * (N+1)

len_burger[0] = 1 # 'P'
patty_cnt[0] = 1

# step 1. 버거와 패티의 개수를 일단 구한다.
for i in range(1, N + 1):
    len_burger[i] = 2 * len_burger[i-1] + 3
    patty_cnt[i] = 2 * patty_cnt[i-1] + 1

# step 2. 버거의 레벨을 안쪽에서 들어가면서 x 개수 만큼 빼고... 패티 개수를 구한다.
# 문제는 패티가 중간에 끊기면..?  그걸 고려하자

def solve(level, x):
    if level == 0:
        if x <= 0:
            # 먹을 것이 없을 경우 패티는 못먹는다.
            return 0
        else:
            # 먹을 것이 있을 경우 최초 레벨 0은 패티 1장
            return 1
    
    # 먹을게 0개일 경우 애초에 못 먹는다.
    if x <= 0:
        return 0
    # 맨 마지막은 무조건 번이다. 패티가 아니므로 카운트가 없다.
    if x == 1:
        return 0 
    
    # 맨 아래 번 ~ 하단 L-1 사이일 경우
    if x <= 1 + len_burger[level - 1]:
        return solve(level - 1, x - 1)
    # 맨 아래 번  ~ 하단 L-1 전체 + 중간에 걸치는 경우
    # 정확하게 패티 개수가 걸치므로. 패티를 바로 반환 가능
    if x == 1 + len_burger[level - 1] + 1:
        return patty_cnt[level - 1] + 1
    # 중간 ~ 상단으로 넘어가는 경우
    if x <= 1 + len_burger[level - 1] + 1 + len_burger[level - 1]:
        return patty_cnt[level - 1] + 1 + solve(
            level-1, x - (1 + len_burger[level - 1] + 1)
        )
    # 마지막 다 먹는 경우
    return patty_cnt[level]

print(solve(N, X))