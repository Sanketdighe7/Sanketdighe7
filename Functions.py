# # Functions are basically some instructions packed together that perform a specific task.
# def hello_func():  # function definition
#     print('Hello')
#     pass
#
#
# print(hello_func)  # it is the function itself
# print(hello_func())  # it is the calling to the function with printing the function itself
# hello_func()  # just calling to the function
#
#
# def hello_func_2():
#     return 'Hello Function 2'  # returns strings
#
#
# hello_func_2()  # this will not print anything because string is just returned but printed
# print(hello_func_2())  # this will print the returned string call by the function
# print(hello_func_2().upper())
# print(len('test'))
#
#
# def hello_fun(greetings, name='You'):
#     return '{}, {}'.format(greetings, name)
#
#
# def student_info(*args, **kwargs):    # within here it's for accepting an arbitrary no. of positional or keyword values.
#     print(args)  # by printing args, its actually a tuple with all f our positional arguments
#     print(kwargs)  # by printing kwargs, is a dictionary with all of our keyword values
#
#
#
# courses = ['math', 'art']
# info = {'name': 'Sanket', 'age': 24}
#
# student_info(courses, info)
# student_info(*courses, **info)  # this is for unpacking the values
#
# student_info('math', 'art', name='Sanket', age=24)
#
# print(hello_fun('Hi', name='Sanket'))


# Code

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


while True:
    print(days_in_month(int(input("Enter year ")), int(input("Enter Month "))))
