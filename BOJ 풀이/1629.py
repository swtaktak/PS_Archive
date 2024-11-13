# A^B mod(C)

def rev_binary_change(x):
    result = ""
    while x > 0:
        if x % 2 == 0:
            result += '0'
        else: result += '1'
        x = x//2
    return result
a, b, c = map(int, input().split())
#step 1. 그냥은 크니까, b를 2진법으로 바꾼다. 역순으로
rev_b = rev_binary_change(b)
# 1승, 2승, 4승, 8승, 16승... 순서로 계산한다. 어디까지? len(rev_b)까지
residue_list = []
for i in range(len(rev_b)):
    if i == 0:
        residue_list.append(a % c)
    else:
        cur_val = ((residue_list[i-1] % c) ** 2) % c
        residue_list.append(cur_val)
        
answer = 1
for i in range(len(rev_b)):
    if rev_b[i] == "1":
        answer = (answer * residue_list[i]) % c
print(answer)