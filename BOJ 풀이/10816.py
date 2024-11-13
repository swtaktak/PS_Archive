num_dict = {}
N = int(input())
num_list = list(map(int, input().split()))
for i in range(0, N):
    if num_list[i] not in num_dict:
        num_dict[num_list[i]] = 1
    else:
        num_dict[num_list[i]] += 1

answer = []
C = int(input())
chk_list = list(map(int, input().split()))
for i in range(0, C):
    if chk_list[i] not in num_dict:
        answer.append(0)
    else:
        answer.append(num_dict[chk_list[i]])

for i in range(0, C):
    if i < C-1:
        print(answer[i], end = ' ')
    else:
        print(answer[i])