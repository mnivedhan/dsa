class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def leaf_node_count(root: Node):
    def dfs(root: Node):
        if not root:
            return 0
        left_count = dfs(root.left)
        right_count = dfs(root.right)
        leaf_count = left_count + right_count
        if right_count == 0 and right_count == 0:
            leaf_count += 1
        return leaf_count
    return dfs(root)


if __name__ == '__main__':
    # _3 = Node(3)
    # _4 = Node(4)
    # _6 = Node(6)
    # _7 = Node(7)
    _2 = Node(2)
    _5 = Node(5)
    _1 = Node(1, _2, _5)
    print(leaf_node_count(root=_1))
