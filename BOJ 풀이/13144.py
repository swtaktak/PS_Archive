import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_visited = [False] * 100000

start = 0
end = 0
answer = 0
while start <= end and end < N:
    if not num_visited[num_list[end]]:
        answer += (end - start + 1)
        num_visited[num_list[end]] = True
        end += 1
    else:
        while num_visited[num_list[end]]:
            num_visited[num_list[start]] = False
            start += 1
print(answer)
            