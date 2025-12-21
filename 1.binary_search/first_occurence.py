def first_occurrence(arr, target):
    left = 0
    right = len(arr)
    first_occurrence_index = -1
    while left < right:
        mid = (left + right)  // 2
        if arr[mid] >= target:
            if arr[mid] == target:
                first_occurrence_index = mid
            right = mid
        else:
            left = mid + 1
    return first_occurrence_index

if __name__ == '__main__':
    arr = [2, 3, 5, 7, 11, 13, 17, 19]
    target = 6
    print(first_occurrence(arr, target))
