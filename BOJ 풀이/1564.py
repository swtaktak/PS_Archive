# 1564
import sys
N = int(input())
ans = 1
for i in range(1, N+1):
    ans *= i
    while ans % 10 == 0:
        ans = ans // 10
    if ans >= 10**12:
        ans = ans % 10**12
ans = str(ans)[-5:]
print(ans)