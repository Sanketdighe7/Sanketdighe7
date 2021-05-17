while True:
    fact = 1
    for i in range(1, int(input("Enter a number: "))+1):
        fact *= i
    print("Factorial of", i, "is", fact)
