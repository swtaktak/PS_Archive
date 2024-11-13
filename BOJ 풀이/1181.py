words = int(input())
word_list = []
for i in range(words):
    cur_word = str(input())
    word_list.append((len(cur_word), cur_word))
word_list = list(set(word_list))
word_list.sort()

for w in word_list:
    print(w[1])