import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def largest_prime_factor(n):
    largest_prime = 0
    # Remove factors of 2
    while n % 2 == 0:
        largest_prime = 2
        n //= 2
    # Check odd factors up to √n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n //= i
    # If n is prime and greater than 2, it is the largest prime factor
    if n > 2:
        largest_prime = n
    return largest_prime

num = 600851475143
print(largest_prime_factor(num))
