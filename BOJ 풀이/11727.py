N = int(input())
ans_list = [0] * (N+1)

for i in range(1, N+1):
    if i == 1:
        ans_list[i] = 1
    elif i == 2:
        ans_list[i] = 3
    else:
        # 세로로 길게 박는 경우 중복 주의
        ans_list[i] = (2 * ans_list[i-2] + ans_list[i-1]) % 10007
print(ans_list[N])


