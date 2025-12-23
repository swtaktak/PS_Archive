# 22357
import sys
input = sys.stdin.readline
MAX = 2500

prime_judge = [True for _ in range(MAX + 1)]
for i in range(2, 51):
    if prime_judge[i]:
        for j in range(i * i, MAX + 1, i):
            prime_judge[j] = False
prime_list = []
for p in range(2001, 2501):
    if prime_judge[p]:
        prime_list.append(p)
print(len(prime_list))

# 64개나 있음 여유로움

box, ball = map(int, input().split())

for i in range(box):
    cur_p = prime_list[i]
    for j in range(1, ball + 1):
        print(1 + cur_p * j, end = " ")
    print()