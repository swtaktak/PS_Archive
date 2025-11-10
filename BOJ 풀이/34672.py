import sys
input = sys.stdin.readline
# 최대 개수는 2의 n승 평태

Q = int(input())
for _ in range(Q):
    row, col, kth = map(int, input().split())
    
    if row == 1 or col % 3 != 0:
        print(-1)
    else:
        blocks = col // 3
        # 최대 개수는 block 단위의 2의 N승 형태
        if kth > 2 ** blocks:
            print(-1)
        # 나머지는 모두 가능함
        else:
            # idea : bitmask.
            kth = kth - 1 # 일단 1을 빼고 비트마스크 해야함
            bitlist = [] # 블록 개수 만큼 채운다 0은 114/144 패턴 1은 322/332 패턴
            row1 = ['0' for _ in range(3 * blocks)]
            row2 = ['0' for _ in range(3 * blocks)]
            
            # bit구하기
            while kth > 0:
                bitlist.append(kth % 2)
                kth = kth // 2
            
            while len(bitlist) < blocks:
                bitlist.append(0)
            
            bitlist.reverse()
            
            for i in range(blocks):
                if bitlist[i] == 0:
                    row1[3 * i] = '1'
                    row1[3 * i + 1] = '1'
                    row1[3 * i + 2] = '4'
                    row2[3 * i] = '1'
                    row2[3 * i + 1] = '4'
                    row2[3 * i + 2] = '4'
                elif bitlist[i] == 1:
                    row1[3 * i] = '3'
                    row1[3 * i + 1] = '2'
                    row1[3 * i + 2] = '2'
                    row2[3 * i] = '3'
                    row2[3 * i + 1] = '3'
                    row2[3 * i + 2] = '2'
            print(''.join(row1))
            print(''.join(row2))                   