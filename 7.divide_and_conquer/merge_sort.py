def merge(left_array, right_array):
    final_array = []
    left_index = right_index =0

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            final_array.append(left_array[left_index])
            left_index += 1;
        else:
            final_array.append(right_array[right_index])
            right_index += 1;

    final_array.extend(left_array[left_index:])
    final_array.extend(right_array[right_index:])

    return final_array

def merge_sort(array):
    """
    Divide stage where all elements are divided and conquered into single element array
    Break down the array into smaller arrays until it become multiple single arrays
    :param array:
    :return:
    """
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    """
    Once multiple single arrays are formed, then conquer and merge two arrays by sorting them 
    """
    return merge(left,right)


if __name__ == "__main__":
    input1= [1, 3, 2, 5, 5, 6]
    # print(merge_sort(input1))
    input2 = [1, 3, 2, 0, 7, 5]
    print(merge_sort(input2))