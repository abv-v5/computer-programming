# function to find all prime numbers up to a given number
def primes_up_to(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            primes.append(num)
    return primes

# Test
print(primes_up_to(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
