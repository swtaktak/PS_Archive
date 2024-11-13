import sys
input = sys.stdin.readline

t_case = int(input())
for _ in range(t_case):
    num_col = int(input())
    line_0 = list(map(int, input().split()))
    line_1 = list(map(int, input().split()))
    
    dp_list = [[0, 0] for _ in range(num_col)]
    
    for i in range(0, num_col):
        if i == 0:
            dp_list[i][0] = line_0[i]
            dp_list[i][1] = line_1[i]
        elif i == 1:
            dp_list[i][0] = dp_list[i-1][1] + line_0[i]
            dp_list[i][1] = dp_list[i-1][0] + line_1[i]
        else:
            # 두 개 앞의 반대줄과 한 개 앞의 반대 줄을 고른다.
            # 두 개 앞의 자기 줄은 볼 필요 없다. 왜냐면, 그걸 본다는 건 한 개 앞의 반대줄을 무시하는 거니까.
            # 이미 최대가 아님이 확정되어 있다.! 점수는 자연수이기 때문이다.
            dp_list[i][0] = max(dp_list[i-2][1], dp_list[i-1][1]) + line_0[i]
            dp_list[i][1] = max(dp_list[i-2][0], dp_list[i-1][0]) + line_1[i]
    print(max(dp_list[-1][0], dp_list[-1][1]))