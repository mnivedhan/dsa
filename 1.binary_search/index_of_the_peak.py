def peak(arr):
    left = 0
    right = len(arr)
    max_index = 0

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid+1]: # Feasible solution arr[i] > arr[i+1]
            max_index = mid
            right = mid
        else:
            left = mid + 1

    return max_index

if __name__ == '__main__':
    arr = [4,8,6,5,3]
    print(peak(arr))
