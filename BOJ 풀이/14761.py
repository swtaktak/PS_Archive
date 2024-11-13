X, Y, N = map(int, input().split())

for i in range(1, N+1):
    if i % X != 0 and i % Y != 0:
        print(i)
    elif i % X == 0 and i % Y != 0:
        print("Fizz")
    elif i % X != 0 and i % Y == 0:
        print("Buzz")
    else:
        print("FizzBuzz")