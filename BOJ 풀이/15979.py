import sys
input = sys.stdin.readline

# idea
# (0, 0) -> 0번
# (0, X)나 (X, 0) -> X가 1이면 1번, 아니면 2번
# (a, b) -> gcd가 1이면 1번, 아니면 2번 # 무한하니까, 하나는 해가 존재할거임 뭐.... 
# (하다못해 1 N 빼서 만들 수 있을거임... 무한하니까)
x, y = map(int, input().split())

def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b > 0:
        a, b = b, a % b
    return a

if x == 0 and y == 0:
    print(0)
elif x == 0:
    if abs(y) == 1:
        print(1)
    else:
        print(2)
elif y == 0:
    if abs(x) == 1:
        print(1)
    else:
        print(2)
else:
    gcd_result = gcd(x, y)
    if gcd_result > 1:
        print(2)
    else:
        print(1)