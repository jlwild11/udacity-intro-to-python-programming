def square_digits(num):
    string = str(num)
    new_string = ""
    for i in string:
        new_string = new_string + str(int(i) * int(i))
    return int(new_string)


test1 = square_digits(9119)
print("expected result: 811181, actual result: {}".format(test1))