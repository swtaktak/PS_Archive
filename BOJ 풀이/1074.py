N, row, col = map(int, input().split())
answer = 0
while N > 0:
    N -= 1
    
    # 2사분면 : 둘다 절반 안넘음
    # 2사분면은, 0배 임
    # *0, *1, *2, *3 이유는... 2*2는 0,1,2,3  4*4는 0,4,8,12  8*8은 0,16,32,48...분해...
    if row < 2 ** N and col < 2 ** N:
        answer += (2 ** N) * (2 ** N) * 0
        
    # 1사분면 : col이 절반을 넘어감, 다음 쪼개기 위해서 col 줄여야 함
    # 1사분면은 1배임
    elif row < 2 ** N and col >= 2 ** N:
        answer += (2 ** N) * (2 ** N) * 1
        col -= (2 ** N)
    
    # 2사분면 : row가 절반을 넘어감
    elif row >= 2 ** N and col < 2 ** N:
        answer += (2 ** N) * (2 ** N) * 2
        row -= (2 ** N)
        
    # 3사분면 : 둘 다 절반을 넘어감
    elif row >= 2 ** N and col >= 2 ** N:
        answer += (2 ** N) * (2 ** N) * 3
        col -= (2 ** N)
        row -= (2 ** N)        
print(answer)