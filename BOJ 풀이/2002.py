import sys
input = sys.stdin.readline
N = int(input())
out_dict = {}
car_name = []
for i in range(N):
    cur_car = str(input().rstrip())
    car_name.append(cur_car)

for i in range(N):
    cur_car = str(input().rstrip())
    out_dict[cur_car] = i
answer = 0
for i in range(1, N):
    flag = False
    cur_car = car_name[i]
    # i가 등수임!
    for j in range(i):
        comp_car = car_name[j] # 더 앞서 있는 차임
        if out_dict[comp_car] > out_dict[cur_car]:
            flag = True
            break
    if flag:
        answer += 1
print(answer)