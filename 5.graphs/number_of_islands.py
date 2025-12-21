from collections import deque

def get_neighbours(vertex, total_rows, total_columns, grid):
    current_row = vertex[0]
    current_column = vertex[1]

    delta_row = [-1, 0, 1, 0]
    delta_column = [0, 1, 0, -1]
    neighbours = []

    for i in range(len(delta_row)):
        neighbour_row = current_row + delta_row[i]
        neighbour_column = current_column + delta_column[i]

        if total_rows > neighbour_row >= 0 and total_columns > neighbour_column >= 0:
            if grid[neighbour_row][neighbour_column] == 1:
                neighbours.append((neighbour_row, neighbour_column))

    return neighbours

def flood_fill(row, column, total_rows, total_columns, grid):
    queue = deque()
    queue.append((row, column))

    visited = set()
    visited.add((row, column))

    grid[row][column] = 0

    while queue:
        vertex = queue.popleft()
        for neighbour in get_neighbours(vertex, total_rows, total_columns, grid):
            if neighbour in visited:
                continue
            queue.append(neighbour)
            visited.add(neighbour)
            grid[neighbour[0]][neighbour[1]] = 0

    return grid

def count_islands(grid: list[list[int]]):
    islands_count = 0
    total_rows = len(grid)
    total_columns = len(grid[0])

    for r in range(total_rows):
        for c in range(total_columns):
            if grid[r][c] == 0:
                continue
            # Once it finds 1 it should flood fill them to 0
            # Increment island count + 1
            grid = flood_fill(r, c, total_rows, total_columns, grid)
            islands_count += 1

    return islands_count

if __name__ == '__main__':
    grid = [[1,1,1,0,0,0], [1,1,1,1,0,0], [1,1,1,0,0,0], [0,1,0,0,0,0], [0,0,0,0,1,0], [0,0,0,0,0,0]]
    print(count_islands(grid))


