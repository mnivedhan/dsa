import heapq


def merge(lists: list[list[int]]):
    result = []
    heap = []

    for input in lists:
        heapq.heappush(heap, (input[0], input, 0))

    while heap:
        min_value, selected_input, selected_index = heapq.heappop(heap)
        result.append(min_value)
        selected_index += 1
        if selected_index < len(selected_input):
            heapq.heappush(heap, (selected_input[selected_index], selected_input, selected_index))

    return result

if __name__ == '__main__':
    inputs = [[1,3,5], [2,4,6], [7,10]]
    print(merge(inputs))