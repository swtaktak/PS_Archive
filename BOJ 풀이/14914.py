import sys
input = sys.stdin.readline
# 2원과 5원을 최소로 써서
# 5원을 최대한 많이 쓴다.
# 안되는거를 2원으로 바꿔서 낸다.

N = int(input())

judge = False
five_coin = N // 5
while five_coin > 0:
    if (N - (5 * five_coin)) % 2 == 0:
        two_coin = (N - (5 * five_coin)) // 2
        judge = True
        break
    five_coin -= 1
    
if judge:
    print(five_coin + two_coin)
else:
    if N % 2 == 0:
        print(N // 2)
    else:
        print(-1)
