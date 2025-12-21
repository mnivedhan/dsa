from collections import deque


def topological_sort(inputs: list[list[int]]):
    nodes = set()
    neighbours = {}
    def neighbours_list():
        for input in inputs:
            child = input[0]
            parent = input[1]
            nodes.add(child)
            nodes.add(parent)
            if neighbours.get(parent):
                neighbours[parent].append(child)
            else:
                neighbours[parent] = [child]


    def find_indegree():
        neighbours_list()
        node_list = list(nodes)
        indegree = {node: 0 for node in node_list}
        for node in node_list:
            for neighbour in neighbours.get(node, []):
                indegree[neighbour] += 1
        return indegree


    queue = deque()
    result = []
    indegrees = find_indegree()
    for node, indegree in indegrees.items():
        if indegree == 0:
            queue.append(node)

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbour in neighbours.get(node, []):
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                queue.append(neighbour)

    return result if len(result) == len(nodes) else None



if __name__ == '__main__':
    print(topological_sort([[1,2], [2,0], [3,1], [3,2]]))

