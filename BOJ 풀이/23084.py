import sys
input = sys.stdin.readline

base = input().rstrip()
base_cnt = [0]*26
for b in base:
    base_cnt[ord(b)-97] += 1

T = int(input())
for _ in range(T):
    after = input().rstrip()
    if len(after) < len(base):
        print("NO")
        continue

    base_len = len(base)
    after_cnt = [0]*26

    for i in range(base_len):
        after_cnt[ord(after[i]) - 97] += 1

    diff_cnt = 0
    for j in range(26):
        if base_cnt[j] > after_cnt[j]:
            diff_cnt += (base_cnt[j] - after_cnt[j])

    flag = False

    # 1트에
    if diff_cnt == 1:
        flag = True
    elif diff_cnt == 0 and len(after) != len(base):
        flag = True


    if not flag:
        for i in range(base_len, len(after)):
            if flag:
                break

            in_j = ord(after[i]) - 97
            out_j = ord(after[i - base_len]) - 97

            # out 처리: after_cnt[out_j] -= 1
            before = max(0, base_cnt[out_j] - after_cnt[out_j])
            after_cnt[out_j] -= 1
            after_need = max(0, base_cnt[out_j] - after_cnt[out_j])
            diff_cnt += (after_need - before)

            # in 처리: after_cnt[in_j] += 1
            before = max(0, base_cnt[in_j] - after_cnt[in_j])
            after_cnt[in_j] += 1
            after_need = max(0, base_cnt[in_j] - after_cnt[in_j])
            diff_cnt += (after_need - before)

            # 판정
            if diff_cnt == 1:
                flag = True
            elif diff_cnt == 0 and len(after) != len(base):
                flag = True

    print("YES" if flag else "NO")
