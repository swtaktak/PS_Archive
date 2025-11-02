import sys
input = sys.stdin.readline

# dp + dfs 형태
def get_ans(m_list, prevprev, prev):
    if m_list == [0, 0, 0, 0, 0]:
        return 1
    
    m1, m2, m3, m4, m5 = m_list
    cur_cnt = dp[m1][m2][m3][m4][m5][prevprev][prev]
    # 이미 구한 패턴이면면
    if cur_cnt != -1:
        return cur_cnt
    
    ans = 0
    for i in range(0, 5):
        if m_list[i] > 0 and prevprev != i and prev != i:
            m_list[i] -= 1
            # 현재 패턴을 깊게 들어가서 구하기
            cnt = get_ans(m_list, prev, i)
            ans += cnt
            m1, m2, m3, m4, m5 = m_list
            dp[m1][m2][m3][m4][m5][prev][i] = cnt
            m_list[i] += 1
    return ans


N = int(input())
sum_marble = 0
m_list = [0 for _ in range(5)]
for i in range(N):
    cur_marble = int(input())
    m_list[i] = cur_marble
    sum_marble += cur_marble

# idea : 7차원 dp를 한다.
# type 1 2 3 4 5, prevprev, prev
dp = [[[[[[[-1 for _ in range(5)] for _ in range(5)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)]

print(get_ans(m_list, -1, -1))