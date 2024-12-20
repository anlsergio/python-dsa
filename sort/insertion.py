def insertion_sort(ll):
    # Time Complexity considerations:
    # As opposed to bubble sort and selection sort, insertion sort
    # has a time complexity of O(n) in case the list is sorted or almost sorted,
    # because the inner loop is conditioned to run only in cases where there is
    # a matching unsorted item.

    # iterate over each element of the list starting from the second element
    for i in range(1, len(ll)):
        # store the current element being sorted in a temporary variable
        temp = ll[i]
        # iterate over the already sorted part of the list
        previous_index = i - 1
        # while the current element is less than the previous element and the index is still in bounds
        while temp < ll[previous_index] and previous_index > -1:
            # swap the current element with the previous element
            ll[previous_index + 1] = ll[previous_index]
            ll[previous_index] = temp
            # decrement the index previous_index
            previous_index -= 1
    # return the sorted list
    return ll


print(insertion_sort([2, 1, 4, 3, 5]))
