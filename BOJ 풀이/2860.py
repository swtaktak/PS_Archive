# idea -> 기약분수 문제
import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

num_list = list(str(input().rstrip()).split('.'))
num_up = int(num_list[0] + num_list[1])
num_down = 10 ** len(num_list[1])
d = gcd(num_up, num_down)
total_sum = num_up // d
total_card = num_down // d

answer = [0] * 6
base = total_sum // total_card
answer[base] = total_card
r = total_sum % total_card
answer[base] -= r
if base < 5:
    answer[base + 1] = r

for i in range(1, 6):
    print(answer[i], end = " ")