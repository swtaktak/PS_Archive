import sys
input = sys.stdin.readline

N, K = map(int, input())
str_a = str(input().rstrip())
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
              'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
# case 1. 만일 N < K 면 볼 것도 없이 실패
# case 2. 만일 K = 1일 경우, A에서 나홀로 있는 문자를 출력한다. 없으면 불가.
# case 3. 만일 K = 2일 경우, 
# case 4. 만일 K >= 3일 경우 비둘기집의 원리에 의해 이웃해있지 않은 조합 발생 확정.
# 정확하게는, 맨 앞의 문자열을 가진 뒤, 

# LANDUARY -> UARY LAND
# SAA AAD   -> AAD SAA