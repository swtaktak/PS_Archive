# 21771
# 가희의 면적과 , 베개의 면적으로 유도 가능
# P의 개수가 부족하다면, 가희가 가린 것 외에는 불가능
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
dr, dc, pr, pc = map(int, input().split())

pillow_cnt = 0
for _ in range(r):
    cur_char = str(input().rstrip())
    for c in cur_char:
        if c == 'P':
            pillow_cnt += 1
            
if pillow_cnt < pr * pc:
    print(1)
else:
    print(0)