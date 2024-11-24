def fib(terms):
    terms[1] = terms[0] + terms[1]
    return terms[1]

twoTerms = [1, 1]
sum = 0
while (sum < 4000000):
    oldVal = twoTerms[1]
    currVal = fib(twoTerms)
    if currVal % 2 == 0:
        sum += currVal
    twoTerms = [oldVal, currVal]

print(sum)