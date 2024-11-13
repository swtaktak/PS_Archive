import sys
input = sys.stdin.readline

F = int(input())
stairs = []
for i in range(F):
    stairs.append(int(input()))
score_list = [0] * F
cur_floor = 0

for i in range(F):
    if i == 0:
        score_list[i] = stairs[0]
    elif i == 1:
        score_list[i] = stairs[0] + stairs[1]
    elif i == 2:
        score_list[i] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    else:
        score_list[i] = max(score_list[i-2], score_list[i-3] + stairs[i-1]) + stairs[i]

print(score_list[F-1])