import sys
input = sys.stdin.readline
lose_score = 0
base_history = [0, 0, 0, 0]

def hit_body(base_history, lose_score):
    global base_history
    global lose_score
    

num_balls = int(input())
hit_body = (base_history, lose_score)