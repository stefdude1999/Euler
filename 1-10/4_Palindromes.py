def isPalindrome(s):
    return s == s[::-1]

largest = 0

for i in range(99, 1000):
    for j in range(99, 1000):
        product = i * j
        if isPalindrome(str(product)) and product > largest:
            largest = product

print(largest)
