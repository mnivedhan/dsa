def longest_subarray(arr, target):
    left = right = 0
    longest = 0
    sum = 0

    while right < len(arr):
        sum += arr[right]
        while sum > target:
            sum -= arr[left]
            left += 1
        longest = max(longest, right - left + 1)
        right += 1

    return longest

if __name__ == '__main__':
    arr = [1, 6, 3, 1, 2, 4, 5]
    target = 10
    print(longest_subarray(arr, target))
