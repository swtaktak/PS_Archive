import sys
input = sys.stdin.readline

# step 1 알파벳을 숫자로.
high_dict = {}
for i in range(26):
    high_dict[chr(ord('A') + i)] = i
    high_dict[chr(ord('a') + i)] = 26 + i
    
mountain = []
rows, cols, diff_cut, timeout = map(int, input().split())

for _ in range(rows):
    cur_row = []
    cur_row_char = str(input().rstrip())
    for c in cur_row_char:
        cur_row.append(high_dict[c])
    mountain.append(cur_row)

INF = 2601*625 + 1

graph = [[INF for _ in range(rows * cols)] for _ in range(rows * cols)]

# step 2. graph 초기화 과정
for i in range(rows):
    for j in range(cols):
        # 일단 자기 자신 -> 자기 자신은 0 해야함
        cur_pos = cols * i + j
        graph[cur_pos][cur_pos] = 0
        
        # 위로 올라갈 수 있니?
        if i > 0:
            next_pos = (i - 1) * cols + j
            # 높이 차이 컷트라인이, 넘어가지 않는다면
            if abs(mountain[i][j] - mountain[i-1][j]) <= diff_cut:
                if mountain[i][j] > mountain[i-1][j]:
                    graph[cur_pos][next_pos] = 1
                    graph[next_pos][cur_pos] = (mountain[i][j] - mountain[i-1][j]) ** 2
                elif mountain[i][j] == mountain[i-1][j]:
                    graph[cur_pos][next_pos] = 1
                    graph[next_pos][cur_pos] = 1
                else:
                    graph[cur_pos][next_pos] = (mountain[i][j] - mountain[i-1][j]) ** 2
                    graph[next_pos][cur_pos] = 1
        
        # 아래로 내려갈 수 있니?
        if i < rows -1:
            next_pos = (i + 1) * cols + j
            # 높이 차이 컷트라인이, 넘어가지 않는다면
            if abs(mountain[i][j] - mountain[i+1][j]) <= diff_cut:
                if mountain[i][j] > mountain[i+1][j]:
                    graph[cur_pos][next_pos] = 1
                    graph[next_pos][cur_pos] = (mountain[i][j] - mountain[i+1][j]) ** 2
                elif mountain[i][j] == mountain[i+1][j]:
                    graph[cur_pos][next_pos] = 1
                    graph[next_pos][cur_pos] = 1
                else:
                    graph[cur_pos][next_pos] = (mountain[i][j] - mountain[i+1][j]) ** 2
                    graph[next_pos][cur_pos] = 1
                    
        # 왼쪽으로 넘어갈 수 있니?
        if j > 0:
            next_pos = cols * i + j - 1
            # 높이 차이 컷트라인이, 넘어가지 않는다면
            if abs(mountain[i][j] - mountain[i][j-1]) <= diff_cut:
                if mountain[i][j] > mountain[i][j-1]:
                    graph[cur_pos][next_pos] = 1
                    graph[next_pos][cur_pos] = (mountain[i][j] - mountain[i][j-1]) ** 2
                elif mountain[i][j] == mountain[i][j-1]:
                    graph[cur_pos][next_pos] = 1
                    graph[next_pos][cur_pos] = 1
                else:
                    graph[cur_pos][next_pos] = (mountain[i][j] - mountain[i][j-1]) ** 2
                    graph[next_pos][cur_pos] = 1
                    
        # 오른쪽으로 넘어갈 수 있니?
        if j < cols-1:
            next_pos = cols * i + j + 1
            # 높이 차이 컷트라인이, 넘어가지 않는다면
            if abs(mountain[i][j] - mountain[i][j+1]) <= diff_cut:
                if mountain[i][j] > mountain[i][j+1]:
                    graph[cur_pos][next_pos] = 1
                    graph[next_pos][cur_pos] = (mountain[i][j] - mountain[i][j+1]) ** 2
                elif mountain[i][j] == mountain[i][j+1]:
                    graph[cur_pos][next_pos] = 1
                    graph[next_pos][cur_pos] = 1
                else:
                    graph[cur_pos][next_pos] = (mountain[i][j] - mountain[i][j+1]) ** 2
                    graph[next_pos][cur_pos] = 1
                    
# step 3 플로이드 와샬 적용
for mid in range(0, rows*cols):
    for left in range(0, rows*cols):
        for right in range(0, rows*cols):
            graph[left][right] = min(graph[left][right], graph[left][mid] + graph[mid][right])

# step 4 정답 도출
max_height = mountain[0][0]
for cur_pos in range(rows*cols):
    cur_row = cur_pos // cols
    cur_col = cur_pos % cols
    if graph[0][cur_pos] + graph[cur_pos][0] <= timeout:
        max_height = max(max_height, mountain[cur_row][cur_col])

print(max_height)