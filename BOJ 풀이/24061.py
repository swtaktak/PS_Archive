# 머지 소트를 배워보자.
# 직접 정렬이 아니다.

def merge_sort(A, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(A, start, mid)
        merge_sort(A, mid+1, end)
        merge(A, start, mid, end)
    return A
    
def merge(A, start, mid, end):
    # 쪼개진 부분을 합치는 코드
    cur_list = []
    left, right = start, mid + 1
    while left <= mid and right <= end:
        if A[left] <= A[right]:
            cur_list.append(A[left])
            left += 1
        else:
            cur_list.append(A[right])
            right += 1
    # 남은 원소 넣기
    while left <= mid:
        cur_list.append(A[left])
        left += 1
    while right <= end:
        cur_list.append(A[right])
        right += 1
    change_s, temp_idx = start, 0
    while change_s <= end:
        A[change_s] = cur_list[temp_idx]
        change_s += 1
        temp_idx += 1

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
num_list = list(map(int, input().split()))
print(merge_sort(num_list, 0, N-1))