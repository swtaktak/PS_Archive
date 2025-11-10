import sys
input = sys.stdin.readline

# 기본 베이스
# 소수 무한성 증명에서 아이디어를 얻어서 푼다.
base = 1
p_list = [True for _ in range(8001)]
p_list[1] = False
for i in range(2, int(8000 ** 0.5) + 1):
    if p_list[i]:
        for j in range(2*i, 8001, i):
            p_list[j] = False
for i in range(2, 8001):
    if p_list[i]:
        base *= i
# 이게 3421자리임
# 무조건 풀리는 값임 ㅋㅋㅋㅋㅋㅋ ㄹㅇㅋㅋ문제.
base = str(base - 1)
# 여기에 10을 곱해도 소인수 2, 5를 곱하는 거라 -1에는 아무런 문제가 없다.

while True:
    n, t = map(int, input().split())
    if n == 0:
        break
    else:
        print(base, end = '')
        for i in range(n - 3421):
            print('9', end = '')
        print()