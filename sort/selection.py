def selection_sort(ll):
    # outer loop will go up to len -1 because
    # there's no reason to go up to the end, because i
    # will be compared to j, which goes up to the end of the list.
    # And the same is for the other way around. "j" starts at i+1, because
    # it will be compared to i anyway.
    for i in range(len(ll) - 1):
        min_index = i
        for j in range(i + 1, len(ll)):
            if ll[j] < ll[min_index]:
                min_index = j
        if min_index != i:
            ll[i], ll[min_index] = ll[min_index], ll[i]

    return ll


print(selection_sort([4, 2, 6, 5, 1, 3]))
