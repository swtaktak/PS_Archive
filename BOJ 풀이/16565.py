num_card = int(input())

if num_card <= 3:
    print(0)
else:
    num_four_card = num_card // 4
    left_card = 52 - num_four_card * 4
    left_pick = num_card - 4 * num_four_card
    
    # nCr = left_pick 