def rotated(arr):
    last_element = arr[-1]
    left = 0
    right = len(arr)
    boundary_index = -1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= last_element: # Feasible solution <= last element of the rotated array
            boundary_index = mid
            right = mid
        else:
            left = mid + 1

    return boundary_index

if __name__ == '__main__':
    arr = [2,3,4,5,1]
    print(rotated(arr))