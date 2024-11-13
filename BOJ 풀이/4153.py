while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        tri_list = [a, b, c]
        tri_list.sort()
        
        if tri_list[0] ** 2 + tri_list[1] ** 2 == tri_list[2] ** 2:
            print('right')
        else:
            print('wrong')