import sys
input = sys.stdin.readline

game, g_p, g_rank = map(int, input().split())
p_rank = [[0, 0, 0, 0, 0] for _ in range(5)]
p_basic_score = [0, 0, 0, 0, 0]

# step 1. 각 게임별 점수 누적을 담는다.
for _ in range(game):
    game_list = [0] + list(map(int, input().split()))
    base_score = [0] + game_list[5:] 
    
    # 등수와 기본 점수를 계산한다.
    # i등 = i번째 값값
    for i in range(1, 5):
        p_rank[game_list[i]][i] += 1
        p_basic_score[game_list[i]] += base_score[i]


# uma를 찾아주자.
uma_success_flag = False
for uma1 in range(100, -101, -1):
    for uma2 in range(uma1, -101, -1):
        for uma3 in range(uma2, -101, -1):
            uma4 = -(uma1 + uma2 + uma3)
            # 우마 네 번째의 조건이 맞는다면
            if -100 <= uma4 <= 100:
                uma_list = [uma1, uma2, uma3, uma4]
                uma_list.sort(reverse = True)
                # 시작 점수 배열을 저장해 놓는다.
                p_score = p_basic_score.copy()
                p_result = []
                for p in range(1, 5):
                    for r in range(1, 5):
                        # 특정 등수를 몇 번? 그 만큼 우마를 먹는다.
                        p_score[p] += (p_rank[p][r] * uma_list[r-1])
                    p_result.append([p_score[p], p])
                p_result.sort(key = lambda x : [-x[0], x[1]])

                if p_result[g_rank -1][1] == g_p:
                    uma_success_flag = True
                    for u in uma_list:
                        print(u, end = " ")
                    exit()
if not uma_success_flag:
    print(-1)