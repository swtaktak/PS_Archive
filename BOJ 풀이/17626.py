# 3은 3개....
# 7이 3개 안됨 8k+7이 소수일 경우 안 됨
# 15의 경우도 3개 안됨
# 두개가 되는 경우가 6은 또. .... 4+1+1 음.
# 아 그 수보다 더 적은 제곱수를 빼고! min + 1을 하면 됨.
# 단 최대는 4

N = int(input())
cnt_list = [0] * (N+1)
for i in range(1, N+1):
    if i == 1:
        cnt_list[i] = 1
    else:
        if (int(i ** 0.5)) ** 2 == i:
            cnt_list[i] = 1
        else:
            cand_list = []
            for j in range(1, int(i**0.5) + 1):
                if i - (j ** 2) >= 0:
                    cand_list.append(cnt_list[i-(j**2)])
            cnt_list[i] = min(4, min(cand_list) + 1)
print(cnt_list[N])