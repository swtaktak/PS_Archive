# IDEA
# BBBBBB... 를 만들고
# A를 땡겨온다. 
# ABBBBB -> A5개
# AABBBB -> 4 * 2가 최대
# AAABBB -> 3 * 3이 최대 -> MAX
# 이렇게 한개씩 줄여나간다. 반절 지점이 최대
# 그래서 만일. 다음 지점과 이번 지점의 사이에서 컷한다.

lens, pair = map(int, input().split())

max_cut = (lens // 2) * (lens - lens // 2)
if pair > max_cut:
    print(-1)
else:
    a_cnt = 0
    b_cnt = lens
    # 현재 a 개수에서 최대로 뽑아낼 수 있는 것은?
    while a_cnt * b_cnt < pair:
        a_cnt += 1
        b_cnt -= 1
        
    # 딱뎀일경우
    if a_cnt * b_cnt == pair:
        ans = 'A' * a_cnt + 'B' * b_cnt
    else:
        # 딱뎀이 아니면, 부족한 개수가 몇개인지 확인한다. 그것이 먼저 나와야 하는 b 개수다.
        front_b = a_cnt * b_cnt - pair
        ans = 'A' * (a_cnt - 1) + 'B' * front_b + 'A' + 'B' * (b_cnt - front_b)
    print(ans)