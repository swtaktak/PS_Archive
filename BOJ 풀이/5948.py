def get_rand(x):
    return ((x % 1000) // 10) ** 2

bitmask = [False] * 10001

x = int(input())
step = 0
while not bitmask[x]:
    bitmask[x] = True
    next_num = get_rand(x)
    x = next_num
    step += 1

print(step)