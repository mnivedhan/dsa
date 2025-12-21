def binary_search(sorted_arr, search_value):
    middle_index = len(sorted_arr)//2
    mid = sorted_arr[middle_index]
    if len(sorted_arr) == 1 and sorted_arr[0] != search_value:
        return False
    if mid == search_value:
        return True
    elif search_value < mid:
        return binary_search(sorted_arr[:middle_index], search_value)
    else:
        return binary_search(sorted_arr[middle_index+1:], search_value)

def binary_search_optimized(sorted_arr, search_value, left=0, right=None):
    if right is None:
        right = len(sorted_arr) - 1
    middle_index = (left+right)//2
    middle_value = sorted_arr[middle_index]
    # Two pointer analogy: if left crosses right(left > right) then no search space, search space exists only when left <= right
    if left > right:
        return False
    if middle_value == search_value:
        return True
    elif search_value < middle_value:
        return binary_search_optimized(sorted_arr, search_value, left, middle_index - 1)
    else:
        return binary_search_optimized(sorted_arr, search_value, middle_index + 1, right)

def binary_search_non_recursive(sorted_arr, search_value):
    left = 0
    right = len(sorted_arr) -1
    while left <= right:
        mid = (left + right)//2
        mid_value = sorted_arr[mid]
        if mid_value == search_value:
            return True
        elif search_value < mid_value:
            right = mid - 1
        else:
            left = mid + 1
    return False

if __name__ == "__main__":
    input = [1,2,3,4,5,6,7,8,9,11]
    print(binary_search(input, 100))
    print(binary_search_optimized(input, 11, 0, None))
    print(binary_search_non_recursive(input, 0))


