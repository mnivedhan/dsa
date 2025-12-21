class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def preorder(node: Node):
    # Base case
    if not node:
        return

    print(node.value) # Actual Logic
    preorder(node.left)
    preorder(node.right)

if __name__ == '__main__':
    node_2 = Node(2)
    node_3 = Node(3)
    node_1 = Node(1, node_2, node_3)
    print(preorder(node_1))