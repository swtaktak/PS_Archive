import sys
input = sys.stdin.readline
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
rows, cols = map(int, input().split())
# 알파벳 지도 만들기
alpha_map = []
for _ in range(rows):
    cur_line = str(input().rstrip())
    alpha_map.append(cur_line)
# 알파벳 중복 체크를 위함, 어차피 이걸 하면 돌아갈 수 없다.
alpha_visit = [False] * 26
# 시작점 세팅 : 좌측 상단 칸 길이 추가에 매우 주의! 
max_length = 0
alpha_visit[ord(alpha_map[0][0]) - 65] = True

def dfs(cur_r, cur_s, alpha_visit, cur_length):
    global max_length
    if cur_length > max_length:
        max_length = cur_length
    for mv in mv_list:
        new_r, new_s = cur_r + mv[0], cur_s + mv[1]
        if 0 <= new_r < rows and 0 <= new_s < cols:
            if not alpha_visit[ord(alpha_map[new_r][new_s]) - 65]:
                alpha_visit[ord(alpha_map[new_r][new_s]) - 65] = True
                dfs(new_r, new_s, alpha_visit, cur_length + 1)
                alpha_visit[ord(alpha_map[new_r][new_s]) - 65] = False
    
dfs(0, 0, alpha_visit, 1)
print(max_length)