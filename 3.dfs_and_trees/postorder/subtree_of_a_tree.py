class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def subtree_check(root, sub_root):
    def is_same_tree(root, sub_root):
        if not root and not sub_root:
            return True
        if not root or not sub_root:
            return False
        return root.value == sub_root.value and is_same_tree(root.left, sub_root.left) and is_same_tree(root.right, sub_root.right)

    if not root:
        return False

    return is_same_tree(root, sub_root) or  subtree_check(root.left, sub_root) or subtree_check(root.right, sub_root)

if __name__ == '__main__':
    _1 = Node(1)
    _2 = Node(2)
    _4 = Node(4, _1, _2)
    _5 = Node(5)
    _3 = Node(3, _4, _5)
    __4 = Node(4, _1, _5)
    print(subtree_check(_3, __4))
