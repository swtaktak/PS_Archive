# 그리디 하게 풀기
import sys
input = sys.stdin.readline
N = int(input())
honey = list(map(int, input().split()))
right_honey = [] # 좌 -> 우
left_honey = []  # 우 -> 좌

for i in range(0, N):
    if i == 0:
        right_honey.append(honey[0])
        left_honey.append(honey[N-1])
    else:
        right_honey.append(honey[i] + right_honey[i-1])
        left_honey.append(honey[N-i-1] + left_honey[i-1])
        
total_honey = right_honey[-1]
max_honey = 0

# 좌 -> 우
for i in range(1, N-1):
    # 한 마리는 맨 왼쪽에서 시작하므로
    first_bee = total_honey - right_honey[0]
    # 두번째 마리가 어디서 시작하자.
    second_bee = total_honey - right_honey[i]
    # 두 번째 벌의 시작점
    cur_honey = first_bee + second_bee - honey[i]
    max_honey = max(cur_honey, max_honey)
# 우 -> 좌
for i in range(1, N-1):
    # 한 마리는 맨 왼쪽에서 시작하므로
    first_bee = total_honey - left_honey[0]
    # 두번째 마리가 어디서 시작하자.
    second_bee = total_honey - left_honey[i]
    # 두 번째 벌의 시작점
    cur_honey = first_bee + second_bee - honey[N-i-1]
    max_honey = max(cur_honey, max_honey)
# 가운데 꿀통
for i in range(1, N-1):
    cur_honey = total_honey + honey[i] - honey[0] - honey[-1]
    max_honey = max(cur_honey, max_honey)
print(max_honey)