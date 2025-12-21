# Problem statement is to find if there are multiple sequence can be formed or only given original sequence can be formed
# Multiple can be formed if the indegree becomes 0 for any two nodes at the same time
from collections import deque


def get_adjacency_list(seqs):
    neighbours = {}
    for seq in seqs:
        parent = seq[0]
        child = seq[1]

        if neighbours.get(parent):
            neighbours[parent].append(child)
        else:
            neighbours[parent] = [child]

    return neighbours

def find_indegree(original, seqs):
    indegree = {task: 0 for task in original}
    for seq in seqs:
        child = seq[1]
        indegree[child] += 1

    return indegree

def sequence_reconstruction(original: list[int], seqs: list[list[int]]):
    neighbours = get_adjacency_list(seqs)
    indegrees = find_indegree(original, seqs)

    result = []

    queue = deque()
    for task, indegree in indegrees.items():
        if indegree == 0:
            queue.append(task)

    while queue:
        if len(queue) > 1:
            return False
        task = queue.popleft()
        result.append(task)
        for neighbour in neighbours.get(task, []):
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                queue.append(neighbour)

    return original == result

if __name__ == '__main__':
    original = [1, 2, 3]
    seqs = [[1, 2], [1, 3], [2, 3]]
    print(sequence_reconstruction(original, seqs))
