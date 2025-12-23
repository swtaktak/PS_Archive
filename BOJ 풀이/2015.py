# 2015
# 단조성이 보장되지 않기 때문에, 다른 풀이가 필요함
# 앞에서 나온 합을 활용하여, 빼줘야 한다.
# 또 자력으로 나오는 경우도 채워야 한다.
# S[i] - S[j] 를 역발상.


N, target = list(map(int, input().split()))

num_list= [0] + list(map(int, input().split()))

ans = 0
sum_cnt = {0 : 1}
cur_sum = 0
for i in range(1, N+1):
    cur_num = num_list[i]
    cur_sum += cur_num
    # 이전거와의 비교를 한다.
    need = cur_sum - target
    if need in sum_cnt:
        ans += sum_cnt[need]
        
    if cur_sum not in sum_cnt:
        sum_cnt[cur_sum] = 1
    else:
        sum_cnt[cur_sum] += 1
print(ans)