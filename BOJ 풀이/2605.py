std = int(input())
jebi_result =list(map(int, input().split()))
answer = []
for i in range(std):
    answer.insert(jebi_result[i], i+1)
answer = answer[::-1]
for i in range(std):
    if i < std-1:
        print(answer[i], end = " ")
    else:
        print(answer[i])