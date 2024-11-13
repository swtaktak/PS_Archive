from collections import deque
N, K = map(int, input().split())
queue = deque()
for i in range(1, N+1):
    queue.append(i)
out_list = []

# 큐 돌리기, 순서대로 다시 넣고 빼면 된다.
# 쉽게 생각하자 쉽게!
while queue:
    for i in range(K-1):
        queue.append(queue.popleft())
    out_list.append(queue.popleft())

# end를 넣으면 줄개행이 일어나지 않음.
print("<", end='')
for i in range(N-1):
    print("%d, "%out_list[i], end='')
print(out_list[-1], end='')
print(">")