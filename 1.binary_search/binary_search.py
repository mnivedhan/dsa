def binary_search(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return target
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return None


if __name__ == "__main__":
    print(binary_search([1,2,3,4,5,6,7], 4))
