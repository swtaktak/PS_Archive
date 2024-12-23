import sys
input = sys.stdin.readline

def dist(x, y):
    return (x ** 2 + y ** 2) ** 0.5

robot = int(input())
time_list = []
for i in range(1, robot + 1):
    x, y, speed = map(int, input().split())
    time_list.append([dist(x, y)/speed, i])

time_list.sort(key = lambda x: (x[0], x[1]))

for t in time_list:
    print(t[1])