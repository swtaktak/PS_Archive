# 수가 너무 커서 inclusion-exclusion 무리 대신 점화식을 생각하자.
# 만일 1번이 2를 고르는 상황에서 2가 1을 고르면 n-2 번째 상황과 동일
# 1번이 2를 고르는 상황에서 2가 1이 아닌 것을 고르면, 1이 빠져버리면 n-1번째와동일
#  why? 1이 2를 가지고, 남은 1번 물건을 2번 물건이라 취급하고 2를 안고른 거니까
# n-1번째와 동일하다.
# WLOG, 대칭성에 의거 1이 고를 2~n  n-1가지 상황에 대칭적으로 적용된다.
std = int(input())
p_list = [0] * (std + 1)
p_list[0] = 0
p_list[1] = 0 
if std >= 2:
    p_list[2] = 1 

for i in range(3, std+1):
    p_list[i] = ((i-1) * (p_list[i-1] + p_list[i-2])) % 1000000000

print(p_list[-1])
