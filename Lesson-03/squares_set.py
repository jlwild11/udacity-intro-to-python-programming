def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2



squares = set()

# todo: populate "squares" with the set of all of the integers less 
# than 2000 that are square numbers

n = 1
while n*n < 2000:
    squares.add(n*n)
    n += 1


print(squares)
