def max_area(arr):

    if len(arr) < 2:
        return 0
    left = 0
    right = len(arr) - 1
    max_area = 0

    while left < right:
        distance = right - left
        volume = arr[left]  if arr[left] < arr[right] else arr[right]
        area = volume * distance
        if area > max_area:
            max_area = area
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return max_area

if __name__ == '__main__':
    arr = [8]
    print(max_area(arr))