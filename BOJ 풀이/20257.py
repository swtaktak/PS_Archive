import itertools
# 20257 문제
a, b, c, d = map(int, input().split())
# 기억을 위함
answer_list = [False] * 10000
answer_count = 0



# step 1 / dfs로 4개의 조합을 모두 던진다.
# 0이 사용되지 않았으므로 걱정없이 조합한다.
num_list = [str(a), str(b), str(c), str(d)]
perm_num_list = list(itertools.permutations(num_list))

# step 2 / 기호 리스트
# 위치 까지 고려를 위함
sym_list = ['+', '*', '-', 'N']
perm_sym_list = list(itertools.product(sym_list, repeat = 3))

for p in perm_num_list:
    # N N N은 기호 안 쓴거는 무효
    for c in perm_sym_list[:-1]:
        cur_form = ''
        for i in range(0, 4):
            if i != 3:
                cur_form += p[i]
                if c[i] != 'N':
                    cur_form += c[i]
            else:
                cur_form += p[3]
        result = eval(cur_form)
        if result >= 0 and not answer_list[result]:
            answer_list[result] = True
            answer_count += 1
print(answer_count)