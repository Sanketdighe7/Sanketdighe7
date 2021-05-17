# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 'Test'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
language = 'c#'
if language == 'python':
    print('language is python')
elif language == 'java':
    print('language is java')
else:
    print('no match')

# and
# or
# not

user = 'admin'
logged_in = False
if not logged_in:
    print('please login')
if user == 'admin' and logged_in:
    print('admin page')
else:
    print("Bad cred's")
print('welcome')

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)

a = [1, 2, 3]       # bcoz these are two different objects in memory
b = [1, 2, 3]
print(a is b)
print(id(a), id(b))
print(id(a) == id(b), '\n')

a = [1, 2, 3]       # now these are the same objects in memory
b = a
print(a is b)
print(id(a), id(b))
print(id(a) == id(b))
