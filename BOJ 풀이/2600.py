import sys
input = sys.stdin.readline
b1, b2, b3 = map(int, input().split())
game_table = [['D' for _ in range(501)] for _ in range(501)]

# 필패
for r in range(b1):
    for c in range(b1):
        game_table[r][c] = 'B'
        
# 모두 A면 B로, 하나라도 B면 A로로
for idx_sum in range(b1, 1001):
    for r in range(0, idx_sum + 1):
        c = idx_sum - r
        if 0 <= r <= 500 and 0 <= c <= 500 and game_table[r][c] == 'D':
            win_judge = False
            for cur_b in [b1, b2, b3]:
                if r - cur_b >= 0:
                    if game_table[r-cur_b][c] == 'B':
                        win_judge = True
                if c - cur_b >= 0:
                    if game_table[r][c-cur_b] == 'B':
                        win_judge = True
            if win_judge:
                game_table[r][c] = 'A'
            else:
                game_table[r][c] = 'B'    
for _ in range(5):
    g1, g2 = map(int, input().split())
    print(game_table[g1][g2])