# 1574
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find_pair(left):
    for right in graph[left]:
        if visited[right]:
            continue
        visited[right] = True
        
        if matchR[right] == -1 or find_pair(matchR[right]):
            matchR[right] = left
            return True
    return False

rows, cols, blanks = map(int, input().split())

if blanks == 0:
    ans = min(rows, cols)
else:
    board = [[1 for _ in range(cols)] for _ in range(rows)]
    for _ in range(blanks):
        r, c = map(int, input().split())
        board[r-1][c-1] = 0
        
    # idea row와 col을 이분매칭시킨다.
    # 겹칠 수 없게 된다. 무조건.
    graph = [[] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 1:
                # row에 연결 가능한 col을 받는다.
                graph[r].append(c)
                
    matchR = [-1 for _ in range(cols)]
    ans = 0

    for left in range(rows):
        visited = [False for _ in range(cols)]
        if find_pair(left):
            ans += 1
print(ans)