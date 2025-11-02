import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())
num_list = list(map(int, input().split()))

# 평균값 계산
cutline = sum(num_list) // N

# 테이블을 최대값이 있는 곳부터 시계방향, 반시계방향으로 나누어 계산
max_idx = num_list.index(max(num_list))

# 시계방향: 최대값 테이블을 기준으로 시작
num_list_clockwise = num_list[max_idx:] + num_list[:max_idx]

# 반시계방향: 최대값 테이블을 기준으로 시작 (시계방향의 반대순서)
num_list_counterclockwise = [num_list_clockwise[0]] + num_list_clockwise[1:][::-1]

# 누적 차이 리스트 생성
diff_list = [num_list_clockwise[0] - cutline]
diff_list_rev = [num_list_counterclockwise[0] - cutline]

for i in range(1, N):
    diff_list.append(diff_list[-1] + num_list_clockwise[i] - cutline)
    diff_list_rev.append(diff_list_rev[-1] + num_list_counterclockwise[i] - cutline)

# 누적 차이의 절댓값 구하기
abs_diff_list = [abs(x) for x in diff_list]
abs_diff_list_rev = [abs(x) for x in diff_list_rev]

# 최종 최소값 출력
print(min(sum(abs_diff_list), sum(abs_diff_list_rev)))
