 
import sys
input = sys.stdin.readline
# 모두 65 빼야함
alpha_draw = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
num_list = []

A = str(input().rstrip())
B = str(input().rstrip())

for i in range(len(A)):
    num_list.append(alpha_draw[ord(A[i]) - 65])
    num_list.append(alpha_draw[ord(B[i]) - 65])

while len(num_list) > 2:
    new_list = []
    for i in range(1, len(num_list)):
        cur_n = (num_list[i-1] + num_list[i]) % 10
        new_list.append(cur_n)
    num_list = new_list.copy()
print(str(num_list[0]) + str(num_list[1]))