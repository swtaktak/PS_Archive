import sys
input = sys.stdin.readline

N = int(input())
answer = [-1] + [-1 for _ in range(N)]
tall_list = [-1] + list(map(int, input().split()))

for cur_person in range(1, N+1):
    cur_jump_need = tall_list[cur_person]
    cur_jump = 0
    cur_pos = 1
    while True:
        if answer[cur_pos] == -1:
            if cur_jump == cur_jump_need:
                answer[cur_pos] = cur_person
                break
            else:
                cur_jump += 1
                cur_pos += 1
        else:
            cur_pos += 1
for a in answer[1:]:
    print(a, end = " ")