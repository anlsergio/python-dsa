################################
# Merge Sort Algorithm
################################

def merge_sort(nums):
    # it will recursively keep breaking the original list in half
    # until there's only 1 item in each list left, which is a sorted list by default.
    # Only then, we start merging the 2 corresponding sorted lists together,
    # until all items are back in the final sorted list.
    if len(nums) == 1:
        return nums
    mid_index = len(nums) // 2
    left = merge_sort(nums[:mid_index])
    right = merge_sort(nums[mid_index:])
    return merge(left, right)


def merge(nums1, nums2):
    combined = []
    i = 0
    j = 0
    # iterate through both lists until one of them is empty.
    while i < len(nums1) and j < len(nums2):
        # given both lists are sorted in ascending order,
        # we add the smaller values of each corresponding lists first
        # and move the corresponding cursor of the list on which the value
        # was added to the combined list.
        if nums1[i] < nums2[j]:
            combined.append(nums1[i])
            i += 1
        else:
            combined.append(nums2[j])
            j += 1

    # once we break out of the loop, that means
    # at least one of those lists is completely empty
    # so it's just a matter of adding the remainder values that are left
    # on the list that still has items because they are naturally greater than
    # the values that are already in the combined list.
    while i < len(nums1):
        combined.append(nums1[i])
        i += 1
    while j < len(nums2):
        combined.append(nums2[j])
        j += 1

    return combined


original_list = [3, 1, 4, 2]
sorted_list = merge_sort(original_list)
print("\nOriginal list: ", original_list)
print("\nSorted list: ", sorted_list)
