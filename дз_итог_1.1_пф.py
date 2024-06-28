def fib(n):
    if n > 0:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
    return a

print(fib(int(input())))