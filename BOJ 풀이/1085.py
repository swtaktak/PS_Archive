import sys
input = sys.stdin.readline

hansu_x, hansu_y, max_w, max_h = map(int, input().split())

answer = min(hansu_x, max_w - hansu_x, hansu_y, max_h - hansu_y)
print(answer)