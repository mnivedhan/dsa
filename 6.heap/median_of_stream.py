import heapq


class MedianOfStream:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def add_number(self, num):
        if len(self.min_heap) == 0 or num < self.min_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        self.balance()

    def balance(self):
        if len(self.min_heap) > len(self.max_heap):
            # move from min to max
            value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -value)
        elif len(self.max_heap) > len(self.min_heap) + 1:
            # Move from max to min
            value = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -value)

    def get_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]

if __name__ == '__main__':
    median = MedianOfStream()
    median.add_number(1)
    median.add_number(2)
    median.add_number(3)
    print(median.get_median())
    median.add_number(4)
    print(median.get_median())

