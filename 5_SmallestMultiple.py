#naive implementation

def isEvenlyDivisible(num):
    for i in range(20, 0, -1):
        if num % i != 0:
            return False
    return True

i = 2520
while True:
    if isEvenlyDivisible(i):
        break
    i += 20

print(i)

