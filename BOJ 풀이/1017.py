import sys
input = sys.stdin.readline

MAX = 2000
prime_check = [True] * (MAX + 1)
prime_check[0] = prime_check[1] = False
for i in range(2, int(MAX ** 0.5) + 1):
    if prime_check[i]:
        for j in range(i * i, MAX + 1, i):
            prime_check[j] = False

def dfs(cur_l):
    for cur_r in graph[cur_l]:
        if visited[cur_r]:
            continue
        visited[cur_r] = True
        if matchR[cur_r] == -1 or dfs(matchR[cur_r]):
            matchR[cur_r] = cur_l
            return True
    return False

N = int(input())
num_list = list(map(int, input().split()))

left = []
right = []

# 첫 번째 수가 속한 쪽을 left로 고정
if num_list[0] % 2 == 0:
    for n in num_list:
        if n % 2 == 0:
            left.append(n)
        else:
            right.append(n)
else:
    for n in num_list:
        if n % 2 == 0:
            right.append(n)
        else:
            left.append(n)

# 홀짝 개수가 다르면 애초에 불가능
if len(left) != len(right):
    print(-1)
    sys.exit(0)

# N == 2 는 그냥 한 쌍만 확인
if N == 2:
    if prime_check[left[0] + right[0]]:
        print(right[0])
    else:
        print(-1)
    sys.exit(0)

L = len(left)
R = len(right)
ans_list = []

for r in range(R):
    # 첫 번째 수(left[0])와 right[r] 를 강제로 짝짓는 경우만 고려
    if not prime_check[left[0] + right[r]]:
        continue

    # 그래프 초기화
    graph = [[] for _ in range(L)]
    for i in range(1, L):
        for j in range(R):
            if j == r:      # 이미 left[0]과 짝이 된 후보는 제외
                continue
            if prime_check[left[i] + right[j]]:
                graph[i].append(j)

    # 이분 매칭
    matchR = [-1] * R
    matchR[r] = 0  # right[r]는 left[0]에 이미 매칭됐다고 생각
    cnt = 1        # 첫 쌍이 이미 매칭됨

    for i in range(1, L):
        visited = [False] * R
        if dfs(i):
            cnt += 1

    if cnt == N // 2:
        ans_list.append(right[r])

if ans_list:
    ans_list.sort()
    print(*ans_list)
else:
    print(-1)
