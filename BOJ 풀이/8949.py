# 대충 더해

a, b = map(int, input().split())
a = str(a)
b = str(b)
len_diff = len(a) - len(b)
if len_diff > 0:
    # a가 더 기니까
    b = ('0' * (len_diff)) + b
elif len_diff < 0:
    # b가 더 기니까
    a = ('0' * (abs(len_diff))) + a
answer = ''
for i in range(len(a)):
    cur_sum = int(a[i]) + int(b[i])
    answer += str(cur_sum)

print(answer)