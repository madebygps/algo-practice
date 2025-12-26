# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)

def fib(n):
    # n = 4
    # 0 1 1 2 3
    a = 0
    b = 1
    result = n

    for _ in range(n - 1):
        result = a + b
        a = b
        b = result
    return result

print(fib(10))


