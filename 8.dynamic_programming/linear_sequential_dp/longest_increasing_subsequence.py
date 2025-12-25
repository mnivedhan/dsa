def solution(array):
    if not array:
        return 0
    if len(array) == 1:
        return 1

    # Initialize result with 1
    result = [1] * len(array)

    # Iterate through array with two pointers.
    # When there is an increasing order do max(existing increasing order for that i, jth index increasing order from 1)
    # As i current item can be solved using on previous item data, this is solved using DP
    for i in range(len(array)):
        j = 0
        while i > j:
            if array[i] > array[j]:
                result[i] = max(result[i], result[j] + 1)
            j += 1

    return max(result)

if __name__ == "__main__":
    input = [3,4,-1,0,6,2,3,4,5,6]
    print(solution(input))