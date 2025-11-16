a = 69230
b = 0
c = 0
loop_cnt = 0
while a > 0:
    loop_cnt += 1
    c = a % 10
    b = 10 * b + c
    a = a // 10
print(loop_cnt)
print(b)
print(a + b + c)