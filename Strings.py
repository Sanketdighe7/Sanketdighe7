message = '''Sanket's "World"'''
print("1 Original Message-->", message)
print("2 message length-->", len(message))
print("3 particular element-->", message[0], "\n5 ----missing---- --> Error")
# print(message[17], "4")                                           # error out of index
print("5 particular length-->", message[3:8])                          # [:5] is same
print("6 to print starting from particular element-->", message[5:])                                             #
print("7 to print last element-->", message[-1])
print("8 -->except last 3 elements", message[0:-3])
print("9 -->to print in between elements", message[-3:-5])
print("10 -->", message[5:-3])
print("11 -->", message[-1:-7])
print("12 Print multiple elements-->", message[0], message[10])
print("13 uppercase-->>", message.upper())
print("14 Lowercase-->>", message.lower())
print("15 to count no. of repeated elements-->", message.count('s'))
print("16 to count no. of repeated elements-->", message.count("World"))
print("17 to find element-->", message.find('World'))
print("18 to find unknown element displays -1 for not found-->", message.find('Universe'))
message = message.replace('World', 'Universe')
print(message)
greetings = "Hello"
name = 'Universe'
msg = greetings + ', ' + name + '. Welcome!'
print(message)
msg1 = '{}, {}. Welcome!'.format(greetings, name)
print(msg1)
msg2 = f'{greetings}, {name}. Welcome!'
print(msg2)
msg3 = f'{greetings}, {name.upper()}. Welcome!'
print(msg3)
print(dir(name))
print(help(str))
print(help(str.lower))
