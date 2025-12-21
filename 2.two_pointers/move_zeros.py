def move_zeroes(arr):
    # slow = 0
    # for fast in range(len(arr)):
    #     if arr[fast] != 0:
    #         arr[slow], arr[fast] = arr[fast], arr[slow]
    #         slow += 1
    slow = fast = 0
    while fast < len(arr):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
        fast +=1
    return arr

if __name__ == "__main__":
    arr = [1,0,2,0,0,7]
    print(move_zeroes(arr))
