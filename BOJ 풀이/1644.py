N = int(input())
prime_list = []
# 앞에 두개 넣고, (0, 1) 나머지를 모두 한다. 그래야 숫자 처럼 사용 가능.
# 이것이 에라토스테네스의 체의 원리, 싹 다 뒤의 배수를 수시로 빼준다.
prime_check = [False, False] + [True] * (N-1)

for i in range(2, N+1):
    if prime_check[i]:
        prime_list.append(i)
        for j in range(2*i, N+1, i):
            prime_check[j] = False
    
start = 0
end = 0
count = 0

while end <= len(prime_list):
    part_sum = sum(prime_list[start:end])
    if part_sum == N:
        count += 1
        end += 1
        
    elif part_sum > N:
        start += 1

    elif part_sum < N:
        end += 1
print(count)