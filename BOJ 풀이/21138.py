import sys
input = sys.stdin.readline
N = int(input())
stack = []  # 스택
answer = 0  # 결과 변수

# 사람들의 키 입력
for _ in range(N):
    cur_num = int(input())
    
    # cur_num보다 작은 값이 있다면 그 값은 이미 이전의 값들과 쌍을 이룬 것
    while stack and stack[-1] < cur_num:
        stack.pop()
        answer += 1  # 쌍을 추가
    
    # 새 값을 스택에 넣기
    if stack:
        answer += 1
    stack.append(cur_num)

# 스택에 남은 값들은 다른 사람들과 쌍을 이룰 수 없으므로 이를 추가할 필요는 없음
print(answer)
'''
import sys
input = sys.stdin.readline
N = int(input())
stack = []  # 스택
answer = 0  # 결과 변수

# 사람들의 키 입력
for _ in range(N):
    cur_num = int(input())
    
    # cur_num보다 작은 값이 있다면 그 값은 이미 이전의 값들과 쌍을 이룬 것
    while stack and stack[-1] < cur_num:
        stack.pop()
        answer += 1  # 쌍을 추가
    
    # 새 값을 스택에 넣기
    stack.append(cur_num)

# 스택에 남은 값들은 다른 사람들과 쌍을 이룰 수 없으므로 이를 추가할 필요는 없음
print(answer)

'''