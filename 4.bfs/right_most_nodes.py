from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_most_nodes(root: Node) -> list[list[int]]:
    result = []
    queue = deque()
    queue.append(root)

    while queue:
        new_level = deque()
        for _ in range(len(queue)): # To split the levels
            node = queue.popleft()
            new_level.append(node.val)
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)

        result.append(new_level[-1])
    return result

if __name__ == '__main__':
    node_6 = Node(6)
    node_7 = Node(7)
    node_8 = Node(8)
    node_5 = Node(5, None, node_8)
    node_4 = Node(4, None, node_7)
    node_3 = Node(3, None, node_6)
    node_2 = Node(2, node_4, node_5)
    node_1 = Node(1, node_2, node_3)
    print(right_most_nodes(node_1))