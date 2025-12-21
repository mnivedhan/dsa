class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def insert(bst: Node, val):
    if not bst:
        return Node(val)

    if bst.value == val:
        return bst

    if bst.value < val:
        bst.right = insert(bst.right, val)
    else:
        bst.left = insert(bst.left, val)

    return bst

if __name__ == '__main__':
    node2 = Node(2)
    node1 = Node(3, left=None, right=node2)
    print(insert(node1, 3))
    # print(insert(node1, 4))