def middle(arr):
    if not arr:
        return None
    slow = fast = 0

    while fast < len(arr) - 1:
        slow += 1
        fast += 2

    return arr[slow]

if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5]
    print(middle(arr))