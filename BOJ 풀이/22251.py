import sys
input = sys.stdin.readline

# 변경 list가 필요하다.
# 노가다해서 셀 수는 없으니, 한번 해보자.
base_light = [0b1110111, 0b0010010, 0b1011101, 0b1011011, 0b0111010, 
              0b1101011, 0b1101111, 0b1010010, 0b1111111, 0b1111011]
base_graph = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        x = base_light[i]
        y = base_light[j]
        base_graph[i][j] = (base_light[i] ^ base_light[j]).bit_count()

# dfs 부분
def dfs(level, pick_list, cur_light):
    global answer
    if sum(pick_list) > max_change:
        return
    if level == digit:
        sum_change = sum(pick_list)
        if 1 <= sum_change <= max_change and 1<= int(cur_light) <= floor_max:
            answer += 1
        return
    
    # 현재 레벨에서 바꿀 것을 결정
    for cur_pos in range(10):
        start_val = int(floor_now[level])
        pick_list.append(base_graph[start_val][cur_pos])
        cur_light += str(cur_pos)
        dfs(level + 1, pick_list, cur_light)
        cur_light = cur_light[:-1]
        pick_list.pop()        


# 변경 가능 최대 층, 전광판 자리 수, 변경 가능 최대 자리 수, 현재 층 위치
floor_max, digit, max_change, floor_now = map(int, input().split())
answer = 0
pick_list = []
cur_light = ''
floor_now = '0'*(digit - len(str(floor_now))) + str(floor_now)
dfs(0, pick_list, cur_light)

print(answer)