import sys
input = sys.stdin.readline

N = int(input())

# S(k)의 길이를 먼저 찾는다.
length = 3
k = 0
while length < N:
    k += 1
    length = 2 * length + (k + 3)

def solve(step, n, length):
    if step == 0:
        return 'm' if n == 1 else 'o'
    
    mid_len = step + 3
    left_len = (length - mid_len) // 2
    
    if n <= left_len:
        return solve(step - 1, n, left_len)
    elif n == left_len + 1:
        return 'm'
    elif left_len + 1 < n <= left_len + mid_len:
        return 'o'
    else:
        return solve(step - 1, n - (left_len + mid_len), left_len)

print(solve(k, N, length))
