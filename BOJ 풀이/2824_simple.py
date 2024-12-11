import sys
from collections import defaultdict
input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b= b, a%b
    return a

# step 1 각각을 소인수분해 해서 넣을 거다.
N = int(input())
N_divs = defaultdict(int)
N_list = list(map(int, input().split()))

M = int(input())
M_divs = defaultdict(int)
M_list = list(map(int, input().split()))

A = 1
B = 1
for n in N_list:
    A *= n
for m in M_list:
    B *= m

ans = gcd(A, B)

if len(str(ans)) <= 9:
    print(ans)
else:
    print(str(ans)[-9:])