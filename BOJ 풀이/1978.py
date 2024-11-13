def is_prime(N):
    if N == 1:
        return False
    else:
        for i in range(2, int(N ** 0.5)+1):
            if N % i == 0:
                return False
    return True
N = int(input())
num_list = list(map(int, input().split()))
cnt = 0
for n in num_list:
    if is_prime(n):
        cnt += 1
print(cnt)