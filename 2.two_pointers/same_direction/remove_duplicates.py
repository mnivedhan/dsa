def remove_duplicates(arr):
    if not arr:
        return len(arr)

    slow = fast = 0

    while fast < len(arr):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]
        fast += 1

    return slow + 1

if __name__ == '__main__':
    # arr = [0, 0, 1, 1, 1, 2, 2, 3]
    arr = [1,1]
    print(remove_duplicates(arr))