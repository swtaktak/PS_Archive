import sys
input = sys.stdin.readline
def round_half_up(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)


a, b = map(int, input().split())
pick = 0
win = 0
card = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
card.remove(a)
card.remove(b)
# 나머지 18개 중 2개를 뽑자
for i in range(17):
    for j in range(i+1, 18):
        pick += 1
        c, d = card[i], card[j]
        
        # 땡인 경우
        if a == b:
            if c != d:
                win += 1
            else:
                if a > c:
                    win += 1
        else:
            if c != d:
                if (a + b) % 10 > (c + d) % 10:
                    win += 1
prob = win/pick
answer = round_half_up(prob * 1000) /1000

print("{:.3f}".format(answer))