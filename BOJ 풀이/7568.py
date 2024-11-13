num = int(input())
human_list = []
for i in range(0, num):
    human_list.append(list(map(int, input().split())))

for i in range(0, num):
    rank = 1
    for j in range(0, num):
        if human_list[i][0] < human_list[j][0] and human_list[i][1] < human_list[j][1]:
            rank += 1
    if i < num - 1:
        print(rank, end = " ")
    else:
        print(rank)