import sys
input = sys.stdin.readline

while True:
    cur_s = str(input().rstrip())
    if cur_s == '*':
        break
    else:
        surprise_flag = True
        if len(cur_s) <= 2:
            surprise_flag = True
        else:
            for i in range(1, len(cur_s)):
                pair_list = []
                if not surprise_flag:
                    break
                else:
                    for j in range(i, len(cur_s)):
                        cur_pair = cur_s[j-i] + cur_s[j]
                        if cur_pair not in pair_list:
                            pair_list.append(cur_pair)
                        else:
                            surprise_flag = False
                            break
        if surprise_flag:
            print("%s is surprising." %(cur_s))
        else:
            print("%s is NOT surprising." %(cur_s))
