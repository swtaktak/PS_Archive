import sys
input = sys.stdin.readline

N = int(input())
# 입력과 상관없이 100만이 대응 되게 하자.

print(2000)
ans_list = []
for i in range(2000):
    if i < 1000:
        ans_list.append(1)
    else:
        ans_list.append(1000)
for a in ans_list:
    print(a, end = " ")