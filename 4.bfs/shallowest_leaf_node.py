import heapq
from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def shallowest_leaf_node(root: Node) -> list[list[int]]:
    queue = deque()
    queue.append(root)
    level = 0
    heap = []
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if not node.left and not node.right:
                heapq.heappush(heap, (level, node.val))
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
        level += 1
    return heapq.heappop(heap)[0]

if __name__ == '__main__':
    node_6 = Node(6)
    node_7 = Node(7)
    node_8 = Node(8)
    node_5 = Node(5, None, node_8)
    node_4 = Node(4, None, node_7)
    node_3 = Node(3, None, node_6)
    node_2 = Node(2, node_4, node_5)
    node_1 = Node(1, node_2, node_3)
    print(shallowest_leaf_node(node_1))