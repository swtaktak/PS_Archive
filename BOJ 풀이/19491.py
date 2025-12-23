import sys
input = sys.stdin.readline

# 10** 18은 18자리... 이거 길어야 자리수 제곱의 합이...
# 81 * 18

MAX = 81 * 18

K, A, B = map(int, input().split())
ans = 0
for i in range(1, MAX + 1):
    # i가 실제로는 함수의 값이 됨
    val = K * i
    if A <= val and val <= B:
        # val의 자리수 제곱합이 실제로 i가 되는지 검토해야함
        cur = val
        sum_sq = 0
        while cur > 0:
            sum_sq += ((cur % 10) ** 2)
            cur = cur // 10
        if sum_sq == i:
            ans += 1
print(ans)