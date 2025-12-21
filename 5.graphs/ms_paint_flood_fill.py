from collections import deque

def get_neighbours(vertex, total_rows, total_columns, original, image):
    current_row = vertex[0]
    current_column = vertex[1]

    delta_row = [-1, 0, 1, 0]
    delta_column = [0, 1, 0, -1]
    neighbours = []

    for i in range(len(delta_row)):
        neighbour_row = current_row + delta_row[i]
        neighbour_column = current_column + delta_column[i]

        if total_rows > neighbour_row >= 0 and total_columns > neighbour_column >= 0:
            if image[neighbour_row][neighbour_column] == original:
                neighbours.append((neighbour_row, neighbour_column))

    return neighbours

def replace(r, c, replacement, image):
    total_rows = len(image)
    total_columns = len(image[0])
    original = image[r][c]
    queue = deque()
    visited = set()
    image[r][c] = replacement
    queue.append((r,c))
    visited.add((r,c))

    while queue:
        vertex = queue.popleft()
        for neighbour in get_neighbours(vertex, total_rows, total_columns, original, image):
            if neighbour in visited:
                continue
            queue.append(neighbour)
            visited.add(neighbour)
            image[neighbour[0]][neighbour[1]] = replacement

    return image

if __name__ == '__main__':
    # image = [[0,1,3,4,1],[3,8,8,3,3],[6,7,8,8,3],[12,2,8,9,1],[12,3,1,3,2]]
    image = [[0,1,0], [1,1,1], [0,1,0]]
    row = 0
    column = 0
    replacement = 9
    print(replace(row, column, replacement, image))