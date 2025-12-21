import heapq


def kth_smallest(matrix: list[list[int]], k):
    heap = []
    tracker = []

    for list in matrix:
        heapq.heappush(heap, (list[0], list, 0))

    while heap:
        min_value, selected_matrix, selected_index =  heapq.heappop(heap)
        tracker.append(min_value)
        if len(tracker) == k:
            return min_value

        selected_index += 1
        if selected_index < len(selected_matrix):
            heapq.heappush(heap, (selected_matrix[selected_index], selected_matrix, selected_index))

    return None

if __name__ == '__main__':
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k  = 8
    print(kth_smallest(matrix, k))