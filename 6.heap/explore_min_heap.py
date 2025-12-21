import heapq


def explore_min_heap():
    min_heap = []
    heapq.heappush(min_heap, 3)
    heapq.heappush(min_heap, 2)
    heapq.heappush(min_heap, 5)
    heapq.heappush(min_heap, 1)
    heapq.heappush(min_heap, 4)

    heapq.heappop(min_heap)
    # heapq.heappop(min_heap)
    # heapq.heappop(min_heap)
    # heapq.heappop(min_heap)
    # heapq.heappop(min_heap)


    print(min_heap)

if __name__ == "__main__":
    explore_min_heap()
