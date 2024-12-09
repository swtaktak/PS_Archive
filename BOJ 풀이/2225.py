n, k = map(int, input().split())
# 소수가 아니어서, 기존 nCk 사용 불가.
# kHn 중복 조합을 구현해야 한다.

ans_list = [[0 for _ in range (n+k)] for _ in range (n+k)]

for i in range(n+k):
    if i == 0:
        ans_list[0][0] = 1
    elif i == 1:
        ans_list[1][0] = 1
        ans_list[1][1] = 1
    else:
        for j in range(0, i+1):
            if j == 0:
                ans_list[i][0] = 1
            elif j < i:
                ans_list[i][j] = (ans_list[i-1][j-1] + ans_list[i-1][j]) % 1000000000
            else:
                ans_list[i][i] = 1
print(ans_list[n+k-1][n] % 1000000000)