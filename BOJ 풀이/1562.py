# bitmasking을 위해 bit연산자를 다룰 줄 알아야 한다.
import sys
input = sys.stdin.readline

bit_range = 1 << 10
d = 10 ** 9
N = int(input())

dp = [[[0]*(bit_range) for _ in range(10)] for _ in range(N + 1)]

# 1자리수 초기화
for k in range(1, 10):
    dp[1][k][1<<k] = 1
    
# 2자리 이상일 때
for digit in range(2, N + 1):
    for cur in range(0, 10):
        for bit in range(bit_range):
            if 0 <= cur < 9:
                plus_1 = bit | 1 << (cur + 1) # 지금까지 한 거에 기억하고, 다음 숫자와 비트 연산을 or 시켜서 집합을 합친다.
                dp[digit][cur + 1][plus_1] += dp[digit - 1][cur][bit]
                dp[digit][cur + 1][plus_1] %= d
            if 0 < cur <= 9:
                minus_1 = bit | 1 << (cur - 1) # 지금까지 한 거에 기억하고, 다음 숫자와 비트 연산을 or 시켜서 집합을 합친다.
                dp[digit][cur - 1][minus_1] += dp[digit - 1][cur][bit]
                dp[digit][cur - 1][minus_1] %= d
                
answer = 0
for k in range(0, 10):
    answer += dp[-1][k][0b1111111111]
    answer %= d
print(answer)