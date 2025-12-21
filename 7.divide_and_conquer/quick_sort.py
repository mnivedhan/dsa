def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array)//2]
    left = []
    right = []
    middle = []
    for x in array:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    # List Comprehension
    # left = [x for x in array if x < pivot]
    # middle = [x for x in array if x == pivot]
    # right = [x for x in array if x > pivot]

    # return quick_sort(left) + quick_sort(middle) + quick_sort(right)
    # Quick sorting middle is not needed as it is always same value so sorting does not make difference
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    input = [1, 0, 2, 5, 4, 7, 6, 9, 8, 3, 1, 2, 12]
    print(quick_sort(input))