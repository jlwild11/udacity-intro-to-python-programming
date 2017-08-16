def nearest_square(limit):
    num = 0
    while (num + 1)**2 < limit:
        num += 1
    return num**2








test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))