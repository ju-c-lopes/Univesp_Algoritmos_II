def bubble_sort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
    return v


print(bubble_sort([4, 9, 4, 7, 48, 12, 24, 40, 88, 32]))
