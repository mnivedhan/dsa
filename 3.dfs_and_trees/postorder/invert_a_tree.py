class Node:
    def __init__(self, val, left= None, right = None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

def invert_tree(root):
    if not root:
        return
    # root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    root.left, root.right = root.right, root.left
    return root

if __name__ == '__main__':
    _3 = Node(3)
    _4 = Node(4)
    _6 = Node(6)
    _7 = Node(7)
    _2 = Node(2, _3, _4)
    _5 = Node(5, _6, _7)
    _1 = Node(1, _2, _5)
    print_tree(_1)
    print("******************")
    print_tree(invert_tree(root=_1))