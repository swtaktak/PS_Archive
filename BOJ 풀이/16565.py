import sys
input = sys.stdin.readline
P = 10007

# 굳이 무리할거 없이, 그냥 52까지이므로 nCk 리스트 가져오자.
nck_list = [[0 for _ in range (53)] for _ in range (53)]

for i in range(53):
    if i == 0:
        nck_list[0][0] = 1
    elif i == 1:
        nck_list[1][0] = 1
        nck_list[1][1] = 1
    else:
        for j in range(0, i+1):
            if j == 0:
                nck_list[i][0] = 1
            elif j < i:
                nck_list[i][j] = (nck_list[i-1][j-1] + nck_list[i-1][j]) % 10007
            else:
                nck_list[i][i] = 1


N = int(input())
if N <= 3:
    print(0)
else:
    ans = 0
    # 포 카드를 1세트 뽑기, 포 카드를 2세트 뽑기, 포 카드를 3세트 뽑기...
    # Inculsion - Exclusion Theorem
    cur_set = 1
    while cur_set * 4 <= N:
        # 13개 세트 중 현재 뽑는 개수 만큼 구하고, 나머지 중 필요한 만큼 뽑기
        cur_cnt = (nck_list[13][cur_set] * nck_list[52 - 4 * cur_set][N - 4 * cur_set]) % 10007
        
        # 홀일 경우 +, 짝일 경우 - 이므로
        if cur_set % 2 == 1:
            ans += cur_cnt
        else:
            ans -= cur_cnt
        
        ans = ans % 10007
        cur_set += 1
    print(ans)