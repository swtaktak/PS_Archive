# 10713
# 새로운 알고리즘을 배운 문제. prefix + 차분
# IDEA : 일차원 선형 구간에서 I ~ J 구간의 +1 변환을 위해..!
import sys
input = sys.stdin.readline

city, day = list(map(int, input().split()))
plan = list(map(int, input().split()))

fair_dict = {}
# 차분 배열 사용을 위해 1번부터 city - 1 로 해야 한다.
for i in range(1, city):
    # 티켓 값, 카드시 통과 비용, 카드 값
    fair_dict[i] = list(map(int, input().split()))

#  문제의 핵심
diff = [0 for _ in range(city + 2)]


for i in range(day - 1):
    start = plan[i]
    end = plan[i + 1]
    
    if start > end:
        start, end = end, start
    
    #  이렇게 할 경우 차분 관점에서 복구해서 보면 start ~ end까지의 값을 +1 얻게 된다.
    # 역 번호라 주의! end 전에서 끝난다.!
    diff[start] += 1
    diff[end] -= 1 
    
ans = 0
cur_cnt = 0
for i in range(1, city):
    cur_cnt += diff[i]
    ans += min(fair_dict[i][0] * cur_cnt, 
               fair_dict[i][1] * cur_cnt + fair_dict[i][2])
print(ans)