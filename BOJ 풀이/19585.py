import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def find_all_prefixes(self, word):
        # 주어진 단어의 모든 가능한 접두사를 찾아야
        node = self.root
        prefixes = []
        for i in range(len(word)):
            c = word[i]
            if c not in node.children:
                break
            node = node.children[c]
            if node.is_end:
                prefixes.append(word[:i+1])  # 가능한 접두사 저장
        return prefixes

color, nick = map(int, input().split())
trie = Trie()
nick_dict = set()

for _ in range(color):
    cur_w = input().strip()
    trie.insert(cur_w)

for _ in range(nick):
    cur_n = input().strip()
    nick_dict.add(cur_n)

Q = int(input())
for _ in range(Q):
    cur_q = input().strip()
    possible_prefixes = trie.find_all_prefixes(cur_q)

    found = False
    for prefix in possible_prefixes:
        remains = cur_q[len(prefix):]
        if remains in nick_dict:
            found = True
            break

    print("Yes" if found else "No")
