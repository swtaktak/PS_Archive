N = int(input())
ans_list = [0] * (N+1)

for i in range(N+1):
    if i == 0:
        ans_list[i] = 0
    elif i == 1:
        ans_list[i] = 1
    elif i == 2:
        ans_list[i] = 2
    else:
        ans_list[i] = (ans_list[i-1] + ans_list[i-2])%10007
print(ans_list[N])