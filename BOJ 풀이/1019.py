import sys
input = sys.stdin.readline

N = int(input())
fact = 1
ans = [0] * 10

while fact <= N:
    # idea / 앞부분, 현재 부분, 뒷 부분을 보면서 계산
    head = N // (fact * 10)
    mid = (N // fact) % 10
    tail = N % fact
    # 1 ~ 9 세기
    for digit in range(1, 10):
        # step 1. head 처리 (앞에 leading - 0 고려)
        ans[digit] += (head * fact)
        # step 2. 현재 mid 만큼 tail이 나와야 한다.
        if digit < mid:
            ans[digit] += fact
        elif digit == mid:
            ans[digit] += (tail + 1) # 0000... tail 세야겠지?
   
    # 0 세기 : leading_zero 주의
    if head != 0:
        ans[0] += (head - 1) * fact
        if mid > 0:
            ans[0] += fact # 그자리 0은 fact 만큼만 나옴
        else:  # cur == 0
            ans[0] += (tail + 1) # 0XX 형태. XX만큼 나와줘야 함
    fact *= 10
            
for a in ans:
    print(a, end = " ")
            
    