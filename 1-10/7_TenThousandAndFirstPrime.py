import math

# using the theory that every prime is 'next to' a multiple of 6 to speed things up
def isPrime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for x in range(6, math.floor(math.sqrt(n)) + 2, 6):
        if n % (x - 1) == 0 or n % (x + 1) == 0:
            return False
    return True

primeCount = 6
count = 11

while primeCount <= 10001:
    count += 1
    if (isPrime(count)):
        primeCount += 1

print(count)