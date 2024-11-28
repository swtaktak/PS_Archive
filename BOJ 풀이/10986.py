import sys
input = sys.stdin.readline

N, div = map(int, input().split())
num_list = list(map(int, input().split()))
res_list = [0]
res_count = [0] * div
res_count[0] += 1
answer = 0
# step 1. 누적합의 리스트를 정리힌다.
for i in range(N):
    cur_residue = (res_list[-1] + num_list[i]) % div
    res_list.append(cur_residue)
    if num_list[i] % div == 0:
        answer += 1
        # 그러나 중복일 경우
        if res_list[-1] == res_list[-2]:
            answer -= 1
    res_count[cur_residue] += 1

for i in range(div):
    if res_count[i] >= 1:
        answer += (res_count[i]) * (res_count[i] - 1) // 2
print(answer)