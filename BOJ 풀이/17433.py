import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        a = int(input())
        print('INFINITY')
    elif N == 2:
        a, b = map(int, input().split())
        if a == b:
            print('INFINITY')
        else:
            print(abs(a-b))
    else:
        num_list = list(map(int, input().split()))
        diff_set = set()
        for i in range(1, N):
            if num_list[i] != num_list[i-1]:
                diff_set.add(abs(num_list[i] - num_list[i-1]))
        diff_set = list(diff_set)
        if len(diff_set) == 0:
            print('INFINITY')
        elif len(diff_set) == 1:
            print(diff_set[0])
        else:
            for i in range(1, len(diff_set)):
                if i == 1:
                    cur_gcd = gcd(diff_set[i], diff_set[i-1])
                else:
                    cur_gcd = gcd(cur_gcd, diff_set[i])
            print(cur_gcd)