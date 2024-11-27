import sys
input = sys.stdin.readline

a = str(input().rstrip())
b = str(input().rstrip())

and_val = ''
for i in range(0, len(a)):
    if a[i] == '1' and b[i] == '1':
        and_val += '1'
    else:
        and_val += '0'

or_val = ''        
for i in range(0, len(a)):
    if a[i] == '1' or b[i] == '1':
        or_val += '1'
    else:
        or_val += '0'

xor_val = ''
for i in range(0, len(a)):
    if (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1'):
        xor_val += '1'
    else:
        xor_val += '0'
        
na_val = ''
for i in range(0, len(a)):
    if a[i] == '1' :
        na_val += '0'
    else:
        na_val += '1'
        
nb_val = ''
for i in range(0, len(b)):
    if b[i] == '1' :
        nb_val += '0'
    else:
        nb_val += '1'

print(and_val)
print(or_val)
print(xor_val)
print(na_val)
print(nb_val)