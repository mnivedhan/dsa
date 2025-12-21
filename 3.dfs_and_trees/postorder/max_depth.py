class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def max_depth(node, node_height = 0):
    if not node:
        return -1

    left_node_height =  max_depth(node.left)
    right_node_height = max_depth(node.right)
    return max(left_node_height, right_node_height) + 1


if __name__ == '__main__':
    node_2 = Node(2)
    node_3 = Node(3)
    node_1 = Node(1, node_2, node_3)
    print(max_depth(node_1))