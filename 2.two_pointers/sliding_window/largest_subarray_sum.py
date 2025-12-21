def subarray_sum_fixed(nums: list[int], k: int) -> int:
    left = 0
    right = left + k
    max_sum = sum(nums[left:right])
    window_sum = max_sum
    while right < len(nums):
        window_sum = window_sum + nums[right] - nums[left]
        if window_sum > max_sum:
            max_sum = window_sum
        left += 1
        right += 1

    return max_sum

if __name__ == '__main__':
    nums = [1, 2, 3, 7, 4, 1]
    k = 3
    print(subarray_sum_fixed(nums, k))