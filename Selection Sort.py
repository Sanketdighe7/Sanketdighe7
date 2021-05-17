lst = [90, 80, 70, 60, 50, 40, 30, 100, 10]
for i in range(len(lst)):
    min_idx = i
    for j in range(i + 1, len(lst)):
        if lst[min_idx] > lst[j]:
            min_idx = j
    lst[i], lst[min_idx] = lst[min_idx], lst[i]
    print(lst)
    print(i, min_idx)
print(lst)