# fibonacci numbers up to n
def fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] + fib_seq[-2] <= n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

# Test
print(fibonacci(20))  # [0, 1, 1, 2, 3, 5, 8, 13]
