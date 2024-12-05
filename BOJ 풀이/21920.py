import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b= b, a%b
    return a

N = int(input())
num_list = list(map(int, input().split()))
X = int(input())
count = 0
sum = 0
for n in num_list:
    if gcd(n, X) == 1:
        count += 1
        sum += n
print(sum/count)