# 랜덤을 고려하지 않는 풀이 2
# 더욱 효율로 간다.
# 아예, 변에 붙여서 441개 / 나머지를 최대한 채운다.
count = 0
for i in range(-8140, 8141, 814):
    for j in range(-8140, 8141, 814):
        print("%d %d" %(i, j))
        count += 1

for i in range(-7733, 7734, 814):
    for j in range(-7733, 7734, 814):
        if count <= 812:
            print("%d %d" %(i, j))
            count += 1
print("%d %d" %(7732, 7734))