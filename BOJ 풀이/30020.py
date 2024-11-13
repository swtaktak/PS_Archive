patty, cheese = map(int, input().split())

if 2*(patty-cheese) > patty or patty <= cheese:
    print("NO")
else:
    print("YES")
    last_plus_size = patty - 2*(patty-cheese) 
    basic_size = patty-cheese
    print(basic_size)
    for i in range(basic_size):
        if i < basic_size - 1:
            print("aba")
        else:
            answer = "ab" + "ab" * last_plus_size + "a"
            print(answer)