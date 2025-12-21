def bubble_up(arr, inserting_value):
    inserting_index = len(arr)

    arr.append(inserting_value)

    while inserting_index > 0:
        parent_index = (inserting_index - 1) // 2
        if arr[parent_index] > inserting_value:
            arr[parent_index], arr[inserting_index] = arr[inserting_index], arr[parent_index]
            inserting_index = parent_index
    return arr

if __name__ == '__main__':
    arr = [8, 10, 9, 12]
    print(bubble_up(arr, 3))