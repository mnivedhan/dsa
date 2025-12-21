class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def pretty_print(node: Node, prefix = ''):
    # Base case (Return vale from child to parent)
    if not node:
        return

    print(prefix + node.value.lower()) # Actual Logic
    prefix += " "
    pretty_print(node.left, prefix ) # State that needs to be passed from parent -> child is sent as parameter
    pretty_print(node.right, prefix)



if __name__ == '__main__':
    node_5 = Node('fuz')
    node_4 = Node('Baz', node_5)
    node_2 = Node('Foo', node_4)
    node_3 = Node('Bar')
    node_1 = Node('/', node_2, node_3)
    print(pretty_print(node_1))