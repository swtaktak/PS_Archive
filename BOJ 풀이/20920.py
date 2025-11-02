import sys
input = sys.stdin.readline

words, min_len = map(int, input().split())
word_dict = {}

for _ in range(words):
    cur_word = str(input().rstrip())
    if len(cur_word) >= min_len:
        if cur_word not in word_dict:
            word_dict[cur_word] = 1
        else:
            word_dict[cur_word] += 1

word_list = []
for w in word_dict:
    word_list.append([w, word_dict[w]])

word_list.sort(key = lambda x: [-x[1], -len(x[0]), x[0]])
for w in word_list:
    print(w[0])