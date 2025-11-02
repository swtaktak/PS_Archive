import sys
input = sys.stdin.readline

N, K = map(int, input().split())
medal_list = []
for _ in range(N):
    ctry, gold, silver, bronze = map(int, input().split())
    medal_list.append([ctry, gold, silver, bronze])
    
medal_list.sort(key = lambda x : [-x[1], -x[2], -x[3]])

medal_rank_list = []
for m in medal_list:
    if not medal_rank_list:
        medal_rank_list.append([m[0], 1])
        prev = m[1:]
    else:
        if m[1:] == prev:
            medal_rank_list.append([m[0], medal_rank_list[-1][1]])
        else:
            medal_rank_list.append([m[0], len(medal_rank_list) + 1])
            prev = m[1:]
    if m[0] == K:
        print(medal_rank_list[-1][1])
        break