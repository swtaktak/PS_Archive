N, K = map(int, input().split())

if K == 0:
    print('B' + 'A' * (N-1))
else:
    flag = False
    for i in range(1, int(K ** 0.5) + 1):
        if K % i == 0:
            left, right = i,  K // i
            if left + right <= N:
                flag = True
                break
    if not flag:
        print(-1)
    else:
        print('B'*(N-left-right) + 'A' * left + 'B' * right)