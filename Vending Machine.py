stock = 10
while stock:
    x = int(input("How many candies do you want: "))
    while stock > 0 and x > 0:
        print("Candy")
        stock -= 1
        x -= 1
print("Out of stock")