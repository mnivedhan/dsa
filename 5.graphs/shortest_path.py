from collections import deque

# Shortest path means **** level check *****
def shortest_path(graph, a, b):

    visited = set()
    queue = deque()
    queue.append(a)
    visited.add(a)

    level =  0
    while queue:
        for _ in range(len(queue)):
            vertex = queue.popleft()
            if vertex == b:
                return level
            for neighbour in graph[vertex]:
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                queue.append(neighbour)

        level += 1

    return level

if __name__ == '__main__':
    adjacency_lists = [[1, 2], [0, 2, 3], [0, 1], [1, 4], [3]]
    start = 0
    end = 4
    print(shortest_path(adjacency_lists, start, end))

