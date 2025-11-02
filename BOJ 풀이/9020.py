import sys
input = sys.stdin.readline

prime_list = {}
num_visited = [True] * 10001
num_visited[0] = False
num_visited[1] = False

for i in range(2, int(10001 ** 0.5) + 1):
    if num_visited[i]:
        for j in range(2*i, 10001, i):
            num_visited[j] = False

T = int(input())

for _ in range(T):
    num = int(input())
    
    for i in range(num // 2, 1, -1):
        if num_visited[i] and num_visited[num - i]:
            print("%d %d" %(i, num-i))
            break
