import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort(reverse = True)
if N % 2 == 0:
    num_list.pop()

sum = 0
for n in num_list:
    if n % 2 == 0:
        sum += (n-1)
    else:
        sum += n
print(sum)