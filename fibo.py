def fib(n):
    result = []

    a, b = 0, 1

    while a < n:
        result.append(a)

        a = b
        b = a + b
    print(result, end = " ")

fib(100)