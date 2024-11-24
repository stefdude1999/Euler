def findTriplet():
    for i in range(1000):
        for j in range(i):
            for k in range(j):
                if (k**2 +j**2 == i**2 and k < j and j < i and i + j + k == 1000):
                    return(i * j * k)

    return 1

print(findTriplet())