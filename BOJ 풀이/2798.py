import sys
input = sys.stdin.readline

def dfs(picked_card, visited):
    global max_score
    
    if sum(picked_card) > goal:
        return
    
    if len(picked_card) == 3:
        if max_score < sum(picked_card):
            max_score = sum(picked_card)
    else:
        for i in range(0, num_cards):
            if not visited[i]:
                picked_card.append(card_list[i])
                visited[i] = True
                dfs(picked_card, visited)
                picked_card.pop()
                visited[i] = False

num_cards, goal = map(int, input().split())
card_list = list(map(int, input().split()))
max_score = 0
picked_card = []
visited = [False] * num_cards
dfs(picked_card, visited)
print(max_score)