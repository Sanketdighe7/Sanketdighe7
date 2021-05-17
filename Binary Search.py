# By Sanket


def BinarySearch(search):
    upp = len(lst)
    low = 0
    while lst[low] <= search <= lst[upp - 1]:
        mid = (upp + low) // 2
        if lst[mid] == search:
            print(search, 'found at', mid + 1)
            break
        elif search < lst[mid]:
            upp = mid
        else:
            low = mid
    else:
        print('Not found')


lst = input("Enter the list elements separated by space: ").split()
print(lst)
BinarySearch(input("Enter Element to be search: "))
