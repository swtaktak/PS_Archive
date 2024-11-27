def binary_change_rev(x):
    ans = ''
    while x > 0:
        if x % 2 == 0:
            ans += '0'
        else:
            ans += '1'
        x = x // 2
    return int(ans)

def ten_to_binary(x):
    x = str(x)
    sum = 0
    for i in range(0, len(x)):
        cur = len(x) - i - 1
        if x[cur] == '1':
            sum += 2 ** i
    return sum

num = int(input())
rev_bin = binary_change_rev(num)
answer = ten_to_binary(rev_bin)
print(answer)