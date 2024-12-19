import sys
input = sys.stdin.readline
target = int(input())
A = int(input())
list_a = list(map(int, input().split()))
B = int(input())
list_b = list(map(int, input().split()))

# 배열 A에서 모든 부분합을 뽑고 개수를 구한다.
# 배열 B에서 모든 부분합을 뽑고, 개수를 구한다.
# A * B 실시한다. 단, 탐색이 쉽게. 

sum_dict_A = {}
for i in range(1, A+1):
    for j in range(0, A-i+1):
        cur_sum = sum(list_a[j:i+j])
        if cur_sum not in sum_dict_A:
            sum_dict_A[cur_sum] = 1
        else:
            sum_dict_A[cur_sum] += 1

sum_dict_B = {}
for i in range(1, B+1):
    for j in range(0, B-i+1):
        cur_sum = sum(list_b[j:i+j])
        if cur_sum not in sum_dict_B:
            sum_dict_B[cur_sum] = 1
        else:
            sum_dict_B[cur_sum] += 1

answer = 0
for a in sum_dict_A:
    if target - a in sum_dict_B:
        answer += (sum_dict_A[a] * sum_dict_B[target-a])
print(answer)
