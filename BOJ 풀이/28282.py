import sys
input = sys.stdin.readline

sock, type = map(int, input().split())
sock_list = list(map(int, input().split()))
left_dict = {}
right_dict = {}
for i in range(sock * 2):
    if i < sock:
        if sock_list[i] not in left_dict:
            left_dict[sock_list[i]] = 1
        else:
            left_dict[sock_list[i]] += 1
    else:
        if sock_list[i] not in right_dict:
            right_dict[sock_list[i]] = 1
        else:
            right_dict[sock_list[i]] += 1
            
count = sock ** 2
for l in left_dict:
    if l in right_dict:
        count -= left_dict[l] * right_dict[l]
print(count)