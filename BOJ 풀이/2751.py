import sys
input = sys.stdin.readline
N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))
num_list.sort(reverse = False)
for n in num_list:
    print(n)