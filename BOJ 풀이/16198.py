import sys
input = sys.stdin.readline


def dfs(marble, cur_energy):
    global max_energy
    if len(marble) == 2:
        if cur_energy > max_energy:
            max_energy = cur_energy
            return
    for i in range(1, len(marble) - 1):
        cur_marble = marble[i]
        add_energy = marble[i-1] * marble[i + 1]
        marble.pop(i)
        dfs(marble, cur_energy + add_energy)
        marble.insert(i, cur_marble)
        
N = int(input())
max_energy = 0
marble = list(map(int, input().split()))
dfs(marble, 0)
print(max_energy)