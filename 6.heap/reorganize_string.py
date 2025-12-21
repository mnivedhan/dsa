import heapq
from collections import Counter


def organize(input):

    str_count = Counter(input)
    heap = []

    for char, count in str_count.items():
        heapq.heappush(heap, (-count, char))

    max_count = -heap[0][0]

    if max_count > (len(input) + 1)  // 2:
        return ""

    result: list[str] = [''] * len(input)

    pointer = 0
    while heap:
        value = heapq.heappop(heap)
        count = -value[0]
        char = value[1]
        for _ in range(count):
            result[pointer] = char
            pointer += 2
            if pointer >= len(input):
                pointer = 1
    return "".join(result)



if __name__ == '__main__':
    input = "aaab"
    print(organize(input))

