def first_true(arr):
    left = 0
    right = len(arr)
    true_index = None

    while left < right:
        mid = (left + right) // 2
        if arr[mid]:
            true_index = mid
            right = mid
        else:
            left = mid + 1

    return true_index

if __name__ == '__main__':
    # arr = [False, False, True, True, True, True]
    # arr = [False, False]
    arr = [False, True]
    print(first_true(arr))