def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


while True:
    print("factorial is ", fact(int(input('Enter a Number '))))
