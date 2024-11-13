import sys
input = sys.stdin.readline
rows, cols, blocks = map(int, input().split())
field = []

for i in range(rows):
    cur_row = list(map(int, input().split()))
    field.append(cur_row)
    
# field를 다 만들었으면 완전 노가다를 하자.
min_time = 257 * 3 * rows * cols
max_height = 0
for cur_height in range (0, 257):
    # 블럭이 부족하다면, 위로 올라갈수록 블록이 그리디하게 부족하다.
    cur_delete = 0
    cur_block = 0
    for i in range(rows):
        for j in range(cols):
            if cur_height > field[i][j]:
                cur_block += (cur_height - field[i][j])
            elif cur_height < field[i][j]:
                cur_delete += (field[i][j] - cur_height)
    if cur_block <= blocks + cur_delete:
        cur_time = cur_delete * 2 + cur_block
        if min_time == cur_time:
            if max_height < cur_height:
                min_time = cur_time
                max_height = cur_height
        elif min_time > cur_time:
            min_time = cur_time
            max_height = cur_height
    else:
        break
print("%d %d" %(min_time, max_height))
