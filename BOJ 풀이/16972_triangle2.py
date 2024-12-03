# 삼각형 배치를 해보자.
# 정삼각형은 아니고, 이등변 삼각형 배치를 먼저 해보자.
'''
a = 1
while True:
    red = (16280//a) * ((16280 // ((3 ** 0.5) * a)) + 1)
    bule = (16280//a + 1) * (((16280-(a * (3 ** 0.5))) // ((3 ** 0.5) * a)) + 1)
    if red + blue < 814:
        break
    a += 1
print(a)
# 627일때 개수가 부족하여 626이 최대 변의 길이임.
# 이등변 삼각형 형태로 최대한 배치하고, 나머지 한 칸만 보정한다.
'''

count = 0
# 윗꼭지점부터 배치
for i in range(-8140, 8141, 627):
    for j in range(-8140, 8140-524, 1050):
        count += 1
        print("%d %d" %(i, j))
# 나머지 꼭지점 배치
for i in range(-8140+313, 8140-312, 627):
    for j in range(-8140+525, 8141, 1050):
        count += 1
        if count < 814:
            print("%d %d" %(i, j))
        elif count == 814:
            print("%d %d" %(i-1, j))
            break 
print(count)