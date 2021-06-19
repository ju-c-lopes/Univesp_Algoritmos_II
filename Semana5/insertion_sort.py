def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]                        # começa com v elemento na posição 1
        j = i-1
        while j >= 0 and x < v[j]:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x
    return v


print(insertion_sort([44, 55, 12, 42, 94, 18, 6, 67]))
