import sys
input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    d, N = map(int, input().split())
    ans_list = []
    
    while N > 0:
        top_digit = int(str(N)[0])
        if N >= top_digit * int('1' * len(str(N))):
            ans_list.append(top_digit * int('1' * len(str(N))))
            N -= top_digit * int('1' * len(str(N)))
        else:
            if top_digit != 1:
                ans_list.append((top_digit-1) * int('1' * len(str(N))))
                N -= (top_digit-1) * int('1' * len(str(N)))
            else:
                ans_list.append(9 * int('1' * (len(str(N))-1)))
                N -= 9 * int('1' * (len(str(N))-1))
    print(len(ans_list))
    for a in ans_list:
        print(a, end =" ")
    print()