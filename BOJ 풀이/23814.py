import sys
input = sys.stdin.readline
mandu = int(input())
jajang, zambong, left = map(int, input().split())
# jajang 채우거나
# zambong 채우거나
# 둘 다 채우거나
# 둘 다 안채우거나
# border = 불가능함.
max_mandu = 0
max_bbok = 0
if left < mandu and (jajang + left) // mandu == 0 and (zambong + left) // mandu == 0:
    print(left)
else:
    cur_mandu = 0
    cur_bbok = 0
    plus_jajang = mandu - (jajang % mandu)
    if left >= plus_jajang:
        cur_mandu += (jajang + plus_jajang) // mandu
        cur_mandu += zambong // mandu
        cur_mandu += (left - plus_jajang) // mandu
    if cur_mandu > max_mandu:
        max_mandu = cur_mandu
        max_bbok = left - plus_jajang
    elif cur_mandu == max_mandu:
        max_bbok = max(max_bbok, left - plus_jajang)  
    
    cur_mandu = 0
    cur_bbok = 0
    plus_zambong = mandu - (zambong % mandu)
    if left >= plus_zambong:
        cur_mandu += (zambong + plus_zambong) // mandu
        cur_mandu += jajang // mandu
        cur_mandu += (left - plus_zambong) // mandu
    if cur_mandu > max_mandu:
        max_mandu = cur_mandu
        max_bbok = left - plus_zambong
    elif cur_mandu == max_mandu:
        max_bbok = max(max_bbok, left - plus_zambong)
            
    cur_mandu = 0
    cur_bbok = 0
    plus_jajang = mandu - (jajang % mandu)
    plus_zambong = mandu - (zambong % mandu)
    if left >= plus_jajang + plus_zambong:
        cur_mandu += (jajang + plus_jajang) // mandu
        cur_mandu += (zambong + plus_zambong) // mandu
        cur_mandu += (left - plus_jajang - plus_zambong) // mandu
    if cur_mandu > max_mandu:
        max_mandu = cur_mandu
        max_bbok = left - plus_jajang - plus_zambong
    elif cur_mandu == max_mandu:
        max_bbok = max(max_bbok, left - plus_jajang - plus_zambong)
            
    cur_mandu = 0
    cur_bbok = 0
    cur_mandu += jajang // mandu
    cur_mandu += zambong // mandu
    cur_mandu += left // mandu
    if cur_mandu > max_mandu:
        max_mandu = cur_mandu
        max_bbok = left
    elif cur_mandu == max_mandu:
        max_bbok = max(max_bbok, left)
    print(max_bbok)