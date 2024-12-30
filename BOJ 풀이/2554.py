# 증명 : 팩토리얼을 묶는다. 5가 더 적다.
# 5의 배수를 꺼내온다..  나머지가 있을 것이다.
# 5의 배수를 묶고, 나머지 부분을 제외하고 몫 부분 만큼 4가 존재한다.
# 그러나 5와 상쇄가 되면서 2가 남는다.
# 5a+b!  = >> 2^a * a! * b!
import sys
input = sys.stdin.readline

N = int(input())
ans = 1
pow_2 = 0
if N == 1:
    print(1)
else:
    while N > 1:
        q, r = N // 5, N % 5
        pow_2 = (pow_2 + q) % 4
        if r <= 1:
            ans *= 1
        elif r == 2:
            ans *= 2
        elif r == 3:
            ans *= 6
        elif r == 4:
            ans *= 4
        ans %= 10
        N = N // 5
    pow_2_list = [6, 2, 4, 8]
    ans = (ans * pow_2_list[pow_2]) % 10
    print(ans)