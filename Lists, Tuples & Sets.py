# Lists [Mutable] Lists allows us to work with list of values. square [] brackets
list_2 = ['History', 'Math', 'Physics', 'CompSci']
list_1 = ['Bio', 'Chemistry']
print(len(list_1))
print(list_1)
print(list_2[2])
print(list_2[-1])
print(list_2[1:3])
print(list_2[2:])
print(list_2[:2])
list_1.append('Art')
print(list_1)
list_1.insert(0, 'English')
print(list_1)
print(list_2[0])
list_2.extend(list_1)
print(list_2)
list_2.insert(0, list_1)
print(list_2)
list_2.remove('Math')
print(list_2)
popped = list_2.pop()
print(popped)
list_2.insert(0, list_1)
print(list_2)
list_2.reverse()
print(list_2)
list_1.sort()
print(list_1)
nums = [8, 1, 7, 3, 4, 9]
print(nums)
nums.sort(reverse=True)
print(nums)
list_1.sort(reverse=True)
print(list_1)
sorted_nums = sorted(list_1)
print(sorted_nums)
sorted_list_1 = sorted(nums)
print(sorted_list_1)
print(min(nums))
print(max(nums))
print(sum(nums))
print(list_1.index('Art'))
# print(list_1.index('PT'))           # Value Error Element is no present in List
print('English' in list_2)
for subject in list_1:
    print(subject, end=' ')
print()
for index, subject in enumerate(list_2, start=1):
    print(index, subject)
list_2_str = ', '.join(list_1)
print(list_2_str)
list_2_str = ' - '.join(list_1)
print(list_2_str)
new_list = list_2_str.split(' - ')
print(new_list)
print(list_2[4])         # Index Error:List Index out of Range
print(list_1)
list_1[0] = 'Art'
list_1[3] = 'English'               # Showing list is muttable
print(list_1)
print(list_2)


# Tuples (Immutable) Tuples allows us to work with sequential data.
# Round () brackets or Parenthesis We can't modify the tuples.
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
# tuple_1[0] = 'Art'          # TypeError: 'tuple' object does not support item assignment
print(tuple_1)                # We can't append anything, remove anything or anything like that
print(tuple_2)
# We can loop through tuples, we can access values and all the other things except for what mutates the list.

# Sets
# Sets are unordered collection of values with no duplicates
# Sets are values that are unordered & also have no duplicates
# Sets Throw away the duplicates.
# It is used to test whether a value is part of set that is membership test.
# Sets determine all the values they either share or don't share with other sets.
# Sets do this lot more efficiently than sets and tuples.
# Sets are optimised for this all
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)
print('Math' in cs_courses)

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


# Empty Lists
empty_list = []     # or
empty_list = list()

# Empty Tuples
empty_tuple = ()    # or
empty_tuple = tuple()

# Empty Sets
empty_set = {}      # This isn't right! It's a dictionary

empty_set = set()   # Correct syntax for defining an Empty Set
