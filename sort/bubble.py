def bubble_sort(ll):
    # start the loop at the end index
    # decrementing by 1 until it gets to 0
    for i in range(len(ll) - 1, 0, -1):
        # each time we decrement from the list
        # we run an inner loop up to the max index of the current outer loop.
        # E.g. if the end index is 5, the inner loop runs up to 5, then 4, then 3,...
        #
        # Each run of the outer loop will get the greatest item and bubble it all the way
        # to the end of the list. By decrementing the outer range, is how we "mark" the last
        # items as sorted.
        for j in range(i):
            # for each time the current item in j is greater than
            # the next element on the list, they need to switch sides
            if ll[j] > ll[j + 1]:
                ll[j], ll[j + 1] = ll[j + 1], ll[j]
    return ll


print(bubble_sort([4, 2, 6, 5, 1, 3]))
