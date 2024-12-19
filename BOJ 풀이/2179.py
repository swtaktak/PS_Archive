import sys
input = sys.stdin.readline


N = int(input())
word_list = []
word_idx = 20001

for i in range(0, N):
    cur_w = str(input().rstrip())
    word_list.append([cur_w, i]) # word index

# 복사해서 정렬로 사용하자.
word_job = word_list.copy()
word_job.sort(key = lambda x: (x[0], x[1]))

# 각각의 단어를 연달아 비교하자.

ans_prefix = ''
ans_idx = 20001
for w in range(1,N):
    prev_word = word_job[w-1][0]
    cur_word = word_job[w][0]
    prev_idx = word_job[w-1][1]
    cur_idx = word_job[w][1]
    if prev_word == cur_word:
        pass
    else:
        cur_len = 0
        for i in range(0, min(len(prev_word), len(cur_word))):
            if prev_word[i] == cur_word[i]:
                cur_len += 1
            else:
                break
        if len(ans_prefix) < cur_len or (len(ans_prefix) == cur_len and ans_idx > min(prev_idx, cur_idx)):
            ans_prefix = cur_word[:cur_len]
            ans_idx = min(prev_idx, cur_idx)

count = 0
for i in range(N):
    if count == 2:
        break
    else:
        cur_word = word_list[i][0]
        if cur_word[:len(ans_prefix)] == ans_prefix:
            if count == 0:
                first = cur_word
                count += 1
            elif count == 1 and cur_word != first:
                second = cur_word
                count += 1
print(first)
print(second)