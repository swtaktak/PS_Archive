# 27162 
# 빡구현 빡구현 신나는 노래 나도 한번 불러본다.

def get_score(dice_list, mode):
    # ones ~ sixs는 개수만큼
    if 0 <= mode < 6:
        return dice_list[mode + 1] * (mode + 1)
    # Four of a kind : 4개 이상의 경우 동일한 주사위 딱 4개의 합
    # 주의 야찌의 경우에도 4개여야 한다.
    elif mode == 6:
        score = 0
        for i in range(1, 7):
            if dice_list[i] >= 4:
                score += (4 * i)
        return score
    # 풀하우스 : 두개짜리와 3개짜리 있나 확인. 둘 다 있는 경우는 단 하나 뿐
    elif mode == 7:
        score = 0
        twos = 0
        threes = 0
        for i in range(1, 7):
            if dice_list[i] == 2:
                twos = i
            if dice_list[i] == 3:
                threes = i
        if twos > 0 and threes > 0:
            score += ((twos * 2) + (threes * 3))
        return score
    # 스몰스트레이트 : 1,2,3,4,5 나오면 30점
    elif mode == 8:
        judge = True
        for i in range(1, 6):
            if dice_list[i] != 1:
                judge = False
                break
        if judge:
            return 30
        else:
            return 0
    # 빅스트레이트는 2,3,4,5,6 이고 30/0  (원본 야찌랑 룰 다름에 주의)
    elif mode == 9:
        judge = True
        for i in range(2, 7):
            if dice_list[i] != 1:
                judge = False
                break
        if judge:
            return 30
        else:
            return 0
    elif mode == 10:
        score = 0
        for i in range(1, 7):
            if dice_list[i] == 5:
                score += 50
        return score
    elif mode == 11:
        score = 0
        for i in range(1, 7):
            score += (dice_list[i] * i)
        return score

jokbo = str(input().rstrip())
dice_list = [0 for _ in range(6 + 1)]
first_three = list(map(int, input().split()))
for f in first_three:
    dice_list[f] += 1
score_max = -1

for new1 in range(1, 7):
    for new2 in range(1, 7):
        dice_list[new1] += 1
        dice_list[new2] += 1
        
        for i in range(len(jokbo)):
            if jokbo[i] == 'Y':
                score_max = max(score_max, get_score(dice_list, i))
        dice_list[new1] -= 1
        dice_list[new2] -= 1
print(score_max)