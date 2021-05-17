nums = [1, 2, 3, 4, 5]
for num in nums:
    print('i am at the start')
    if num == 3:
        print(3, 'found 3')
        break
    print(num, 'i am in for but not in if')
print('i am out of for')


# x = 0
#
# while True:
#     # if x == 5:
#     #     break
#     print(x)
#     x += 1

for num in nums:
    for letter in 'abc':
        print(letter, num)

for i in range(1, 11):
    print(i)

x = 0
while x < 10:
    if x == 5:
        print(x)
    x += 1

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1
