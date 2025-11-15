a = 69230
b = 0
c = 0
while a > 0:
    c = a % 10
    b = 10 * b + c
    a = a // 10
print(a + b + c)