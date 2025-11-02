import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
cutline = sum(num_list) // N

diff_cc = []
max_diff_cc = -897687543217
max_idx_cc = -1

# 시계 방향향
# 편차 업데이트, 최대 편차 찾기
for i in range(N):
    if i == 0:
        diff_cc.append(num_list[0] - cutline)
    else:
        diff_cc.append(num_list[i] - cutline + diff_cc[-1])
    if diff_cc[i] > max_diff_cc:
        max_diff_cc = diff_cc[i]
        max_idx_cc = i

max_idx_cc = max_idx_cc + 1
ans_cc = 0
carry_cc = 0
for i in range(0, N):
    ans_cc += carry_cc
    carry_cc += (num_list[(max_idx_cc + i) % N] - cutline)
    
# 반반시계 반대대향향
# 편차 업데이트, 최대 편차 찾기
diff_acc = [ -897687543217 for _ in range(N)]
max_diff_acc = -897687543217
max_idx_acc = -1
for i in range(N-1, -1, -1):
    if i == N-1:
        diff_acc[i] = num_list[N-1] - cutline
    else:
        diff_acc[i] = num_list[i] - cutline + diff_acc[i + 1]
    if diff_acc[i] > max_diff_acc:
        max_diff_acc = diff_acc[i]
        max_idx_acc = i
        
max_idx_acc = max_idx_acc - 1
ans_acc = 0
carry_acc = 0
for i in range(0, N):
    ans_acc += carry_acc
    carry_acc += (num_list[(max_idx_acc - i) % N] - cutline)
    
print(min(abs(ans_cc), abs(ans_acc)))