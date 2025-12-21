from collections import deque


def find_neighbours(requirements: list[list[str]]):
    neighbours = {}
    for req in requirements:
        if neighbours.get(req[0]):
            neighbours[req[0]].append(req[1])
        else:
            neighbours[req[0]] = [req[1]]

    return neighbours


def find_indegree(tasks:list, requirements: list[list[str]]):
    indegree = {task: 0 for task in tasks}

    for req in requirements:
        indegree[req[1]] += 1

    return indegree

def task_scheduler(tasks: list, requirements: list[list[str]]):

    indegrees = find_indegree(tasks, requirements)
    neighbours = find_neighbours(requirements)
    result = []

    queue = deque()
    for task, indegree in indegrees.items():
        if indegree == 0:
            queue.append(task)

    while queue:
        task = queue.popleft()
        result.append(task)

        for neighbour in neighbours.get(task, []):
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                queue.append(neighbour)

    return result if len(result) == len(tasks) else None


if __name__ == '__main__':
    tasks = ["a", "b", "c", "d"]
    requirements = [["a", "b"], ["c", "b"], ["b", "d"]]
    print(task_scheduler(tasks, requirements))
