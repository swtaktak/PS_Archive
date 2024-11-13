import sys
input = sys.stdin.readline

house = int(input())
paint_line = [0, 0, 0]

for i in range(house):
    cur_paint = list(map(int, input().split()))
    
    if i == 0:
        paint_line[0] = cur_paint[0]
        paint_line[1] = cur_paint[1]
        paint_line[2] = cur_paint[2]
    else:
        new_paint_line = [0, 0, 0]
        new_paint_line[0] = cur_paint[0] + min(paint_line[1], paint_line[2])
        new_paint_line[1] = cur_paint[1] + min(paint_line[0], paint_line[2])
        new_paint_line[2] = cur_paint[2] + min(paint_line[0], paint_line[1])
        paint_line = new_paint_line
print(min(paint_line))