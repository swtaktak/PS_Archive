import sys
input = sys.stdin.readline

seg_list = []
N = int(input())
for _ in range(N):
    s, e = map(int, input().split())
    seg_list.append([s, e])

seg_list.sort(key = lambda x: (x[0], x[1]))

answer = 0
for i in range(N):
    if i == 0:
        cur_s = seg_list[i][0]
        cur_e = seg_list[i][1]
    else:
        # 현재 끝 점이, 다음 세그먼트의 시작점보다 뒤에 있다면?
        if cur_e >= seg_list[i][0]:
            cur_e = max(seg_list[i][1], cur_e)
            cur_s = min(seg_list[i][0], cur_s)
        
        # 만일 아니라면, answer에 추가하고 cur_s, cur_e를 
        else:
            cur_seg = cur_e - cur_s
            answer += cur_seg
            cur_s = seg_list[i][0]
            cur_e = seg_list[i][1]
# 마지막 거 추가
answer += (cur_e - cur_s)
print(answer)
