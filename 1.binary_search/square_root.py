def sqrt(target):
    left = 0
    right = target + 1
    ans = -1

    while left < right:
        mid = (left + right) // 2
        if mid * mid == target:
            return mid
        elif mid * mid > target:
            ans = mid
            right = mid
        else:
            left = mid + 1

    return ans - 1

if __name__ == '__main__':
    print(sqrt(15))