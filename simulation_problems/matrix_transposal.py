def transpose(matrix):
    transposed = zip(*matrix)
    return [list(row) for row in transposed]

if __name__ == '__main__':
    print(transpose([[1,2,3],[4,5,6]]))