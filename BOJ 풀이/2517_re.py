import sys
input = sys.stdin.readline

N = int(input())
num_list = [int(input()) for _ in range(N)]

# 좌표압축
sorted_list = sorted(num_list)
abil_idx = {v: i + 1 for i, v in enumerate(sorted_list)}  # 1..N

# 세그트리 준비
size = 1
while size <= N:
    size *= 2
tree = [0] * (2 * size)
base = size - 1  # 네 코드의 size -= 1 개념을 base로 명확히

def tree_update(idx):
    idx += base
    tree[idx] += 1
    idx //= 2
    while idx >= 1:
        tree[idx] = tree[2 * idx] + tree[2 * idx + 1]
        idx //= 2

def tree_interval_sum(idx):
    # idx..N 의 합 (idx가 N+1이면 0이 나와야 함)
    if idx > N:
        return 0
    left = idx + base
    right = N + base
    ans = 0
    while left <= right:
        if left % 2 == 1:
            ans += tree[left]
            left += 1
        left //= 2

        if right % 2 == 0:
            ans += tree[right]
            right -= 1
        right //= 2
    return ans

out = []
seen = 0
for v in num_list:
    cur_idx = abil_idx[v]

    # 앞에 있는 선수들 중 "나보다 강한(>)" 사람 수 = (cur_idx+1..N)
    stronger = tree_interval_sum(cur_idx + 1)
    out.append(str(stronger + 1))

    tree_update(cur_idx)
    seen += 1

sys.stdout.write("\n".join(out))
