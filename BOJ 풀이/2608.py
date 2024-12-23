# 로마 숫자 문제

import sys
input = sys.stdin.readline
rome_dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L': 50,
             'C' : 100, 'D' : 500, 'M' : 1000}
rev_dict = {'IV' : 4, 'IX' : 9, 'XL' : 40, 
            'XC' : 90, 'CD' : 400, 'CM': 900}

def rome_to_num(s):
    num = 0
    if len(s) == 1:
        return rome_dict[s]
    else:
        cur_pos = 0
        while cur_pos < len(s):
            if cur_pos + 2 <= len(s) and s[cur_pos:cur_pos+2] in rev_dict:
                num += rev_dict[s[cur_pos:cur_pos + 2]]
                cur_pos += 2
            else:
                num += rome_dict[s[cur_pos]]
                cur_pos += 1
    return num
            
def num_to_rome(n):
    ans = ''
    if n // 1000 > 0:
        ans += 'M' * (n//1000)
        n = n % 1000
    if n >= 900:
        ans += 'CM'
        n -= 900
    if n >= 500:
        ans += 'D'
        n -= 500
    if n >= 400:
        ans += 'CD'
        n -= 400
    if n // 100 > 0:
        ans += 'C' * (n//100)
        n = n % 100
    if n >= 90:
        ans += 'XC'
        n -= 90
    if n >= 50:
        ans += 'L'
        n -= 50
    if n >= 40:
        ans += 'XL'
        n -= 40
    if n // 10 > 0:
        ans += 'X' * (n//10)
        n = n % 10
    if n >= 9:
        ans += 'IX'
        n -= 9
    if n >= 5:
        ans += 'V'
        n -= 5
    if n >= 4:
        ans += 'IV'
        n -= 4
    if n >= 1:
        ans += 'I' * n
    return ans

s1 = str(input().rstrip())
s2 = str(input().rstrip())

n1 = rome_to_num(s1)
n2 = rome_to_num(s2)
print(n1 + n2)
print(num_to_rome(n1 + n2))    