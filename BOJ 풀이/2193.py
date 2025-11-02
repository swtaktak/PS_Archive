import sys
input = sys.stdin.readline

N = int(input())
dp_list = []

# 끝이 zero / one
# 역으로 앞 두개/ 하개를 보는 방식
# 아! 피보나치!
for i in range(N+1):
    if i == 0:
        dp_list.append(0)
    elif i == 1:
        dp_list.append(1)
    else:
        dp_list.append(dp_list[i-1] + dp_list[i-2])

print(dp_list[-1])
