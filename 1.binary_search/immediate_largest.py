def get_first_largest(arr, target):
    left = 0
    right =  len(arr)
    first_largest_index = -1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target or arr[mid] == target: ## This is feasible function to check for monotonic
            first_largest_index = mid
            right = mid
        else:
            left = mid + 1
    return first_largest_index

if __name__ == '__main__':

    print(get_first_largest([1,3,3,5,7], 2))
