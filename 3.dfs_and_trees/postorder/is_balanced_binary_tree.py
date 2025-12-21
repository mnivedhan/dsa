class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def balanced_binary_tree(node: Node):
    def check(node: Node):
        # base case
        if not node:
            return True, -1

        left_balanced, left_height = check(node.left)
        right_balanced, right_height = check(node.right)

        node_balanced = left_balanced and right_balanced and (abs(left_height-right_height) <= 1)
        node_height = max(left_height, right_height) + 1
        return node_balanced, node_height

    return check(node)[0]

if __name__ == '__main__':
    node_8 = Node(8)
    node_7 = Node(7)
    node_6 = Node(6, node_8, None)
    node_5 = Node(5)
    node_4 = Node(4, None, node_7)
    node_2 = Node(2, node_4, node_5)
    node_3 = Node(3, None, node_6)
    node_1 = Node(1, node_2, node_3)
    print(balanced_binary_tree(node_1))

