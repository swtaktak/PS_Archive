import sys
input = sys.stdin.readline

def cantor(left, right):
    if right - left == 1:
        return
    mid_left = left + (right - left) // 3
    mid_right = left + (right - left) // 3 * 2
    
    for m in range(mid_left, mid_right):
        cantor_list[m] = ' '
    
    cantor(left, mid_left)
    cantor(mid_right, right)

while True:
    line = input()
    if not line:
        break  # EOF
    
    N = int(line)
    if N == 0:
        print('-')
        continue
    
    cantor_list = ['-'] * (3 ** N)
    cantor(0, 3 ** N)
    print(''.join(cantor_list))
