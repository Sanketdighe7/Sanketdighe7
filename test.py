# def div(a, b):
#   if a < b:
#        a, b = b, a
# return print(a/b)


# div(16, 64)
# attributes which are variables
# and behaviour which are methods(functions)

class computer:
    def config(self):
        print('i5, 16GB, 1TB')


com1 = computer()
com2 = computer()
computer.config(com1)
computer.config(com2)
com1.config()
com2.config()


# lambda
def square(a):
    return a * a  # functions are objects in python


result = square(5)
print(result)

f = lambda a: a * a
result = f(5)
print(result)
f = lambda a, b: a + b
result = f(5, 6)
print(result)


# lambda filter map & reduce
def is_even(n):
    return n % 2 == 0


def update(n):
    return n * 2


from functools import reduce


def add_all(a, b):
    return a + b


nums = [2, 3, 4, 5, 2, 4, 5, 3, 8, 1, 5, 7, 9, 1, 6]
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)
doubles = list(map(update, evens))
doubles = list(map(lambda n: n * 2, evens))
print(doubles)
sum = reduce(add_all, doubles)
sum1 = reduce(lambda a, b: a + b, doubles)
print(sum1)


# decorators using decorators we can add extra features in the existing functions
def div(a, b):
    print("4", a / b)


def smart_div(func):  # decorator function
    def inner(a, b):
        if a < b:
            a, b = b, a
            print("3")
            return func(a, b)
    print("2")
    return inner


print("1")
div = smart_div(div)
div(2, 4)
