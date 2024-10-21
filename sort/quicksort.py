#####################################
# Quicksort List Comprehension Algorithm
#####################################
def quicksort_list_comp(nums):
    if len(nums) < 2:
        return nums
    pivot = nums[0]
    less_than = [i for i in nums[1:] if i <= pivot]
    more_than = [i for i in nums[1:] if i > pivot]
    return quicksort_list_comp(less_than) + [pivot] + quicksort_list_comp(more_than)


print("\nQuicksort list comprehension:")
print(quicksort_list_comp([5, 3, 6, 8, 1, 2]))


#####################################
# Quicksort in place Algorithm
#####################################
def quicksort_in_place(nums):
    def quicksort(nums, start_idx, end_idx):
        # if the starting index is greater than the ending index,
        # this means we are done, because there are no elements left to process.
        if start_idx > end_idx:
            return nums
        # pivot() rearranges the list delimited by the starting and ending indexes
        # and returns the position where the pivot is located at.
        pivot_index = pivot(nums, start_idx, end_idx)
        # recursively rearrange the elements to the left of the current pivot.
        quicksort(nums, start_idx, pivot_index - 1)
        # recursively rearrange the elements to the right of the current pivot.
        quicksort(nums, pivot_index + 1, end_idx)
        # return the current state of nums.
        return nums

    # initialize the recursive call delimiting the start and end indexes
    # to the entire list.
    return quicksort(nums, 0, len(nums) - 1)


def pivot(nums, start_idx, end_idx):
    # pivot rearranges the list nums in a way that
    # all elements smaller than pivot are moved to its left
    # and all elements greater than pivot are moved to its right
    # returning the index where the pivot is located at after the
    # rearrangement.

    # swap index is the cursor marking where the swap needs to happen.
    # it's initialized at the same position as the pivot, which in this case, is
    # the starting position where the loop will start out.
    swap_index = start_idx
    pivot_index = start_idx
    # loop through the nums list at the starting position defined by pivot index
    # up to the right_index delimiter.
    for i in range(pivot_index + 1, end_idx + 1):
        # if the element in "i" is smaller than the pivot,
        # it should be moved to the left.
        # At this point, pivot will remain in the starting position,
        # to make the rearrangement easier to manage.
        if nums[i] < nums[pivot_index]:
            # move swap index to the right, so that it doesn't affect the pivot position
            # nor the item that was already swapped by a previous iteration.
            swap_index += 1
            # swap the elements in "i" and in "swap_index"
            nums[i], nums[swap_index] = nums[swap_index], nums[i]
    # when all elements are properly rearranged (smaller elements to the left, greater to the right)
    # it's time to swap the pivot, which was kept at the starting position, to the middle of the list,
    # which is where the swap_index cursor was left last.
    nums[pivot_index], nums[swap_index] = nums[swap_index], nums[pivot_index]
    # swap index is where the pivot is located at after the last swap.
    return swap_index


print("\nQuicksort in place:")
print(quicksort_in_place([4, 6, 1, 7, 3, 2, 5]))
