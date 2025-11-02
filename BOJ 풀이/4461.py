import sys
input = sys.stdin.readline

def solve(N):
    global ans_a, ans_b, ans_c
    min_sum = 4000
    cutline = min(int(4000 / int((1 + 2 * ((N / 2) ** 0.5)) ** (1/3))) + 1, 2000)
    for b in range(1, cutline):
        cur_sum = N * (b ** 3)
        for c in range(1, int((cur_sum/2)  ** (1/3)) + 1):
            a_cubed = cur_sum - c ** 3
            a = max(int(a_cubed ** (1/3)) - 1, 0)
            success_flag = True
            while True:
                if a ** 3 < a_cubed:
                    a += 1
                elif a ** 3 > a_cubed:
                    success_flag = False
                    break
                else:
                    break
            if success_flag:
                if a + b + c < min_sum and a >= c:
                    ans_a = a
                    ans_b = b
                    ans_c = c
                    min_sum = a + b + c
        if min_sum < b:
            break                 
           

while True:
    ans_a = -1
    ans_b = -1
    ans_c = -1
    N = int(input())
    if N == 0:
        break
    else:
        solve(N)

        if ans_a == -1:
            print('No value.')
        else:
            print('(%d/%d)^3 + (%d/%d)^3 = %d' %(ans_a, ans_b, ans_c, ans_b, N))