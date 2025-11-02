import sys
input = sys.stdin.readline

N = int(input())
print('Gnomes:')
for _ in range(N):
    num_list = list(map(int, input().split()))
    
    if num_list == sorted(num_list) or num_list == (sorted(num_list, reverse=True)):
        print('Ordered')
    else:
        print('Unordered')