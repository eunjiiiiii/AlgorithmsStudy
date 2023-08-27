def fib(N: int) -> int:
    x, y = 0, 1

    for i in range(0, N):
        x, y = y, x + y

    return x

n = int(input())
print(fib(n))

