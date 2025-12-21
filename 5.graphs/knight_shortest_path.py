from collections import deque


def get_neighbours(vertex):
    row = vertex[0]
    column = vertex[1]

    neighbours = []

    delta_rows = [-2, -2, -1, 1, 2, 2, 1, -1]
    delta_columns = [-1, 1, 2,2,1,-1,-2,-2]

    for i in range(len(delta_rows)):
        neighbour_row = row + delta_rows[i]
        neighbour_column = column + delta_columns[i]
        neighbours.append((neighbour_row, neighbour_column))
    return neighbours

def shortest_path(x: int, y: int):
    queue = deque()
    queue.append((0,0))

    visited = set()
    visited.add((0,0))

    steps = 0
    while queue:
        for _ in range(len(queue)):
            vertex = queue.popleft()
            if vertex == (x, y):
                return steps

            for neighbour in get_neighbours(vertex):
                if neighbour in visited:
                    continue
                queue.append(neighbour)
                visited.add(neighbour)
        steps += 1

    return steps

if __name__ == '__main__':
    print(shortest_path(6,9))