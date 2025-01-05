import sys
input = sys.stdin.readline
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def get_sqrt(x):
    # 시작점 약간 보정하여 진행.
    ans = max(int(x**0.5)-2, 0)
    while ans ** 2 <= x:
        ans += 1
    return ans - 1
a, b = map(int, input().split())

success = int(get_sqrt(b)) - int(get_sqrt(a))
if success == 0:
    print(0)
else:
    d = gcd(success, b - a)
    print("%d/%d" % (success//d, (b-a)//d))