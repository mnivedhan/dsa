class Node:
    def __int__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(tree: Node):
    if not tree:
        return True


    left_valid = valid_bst(tree.left)
    right_valid = valid_bst(tree.right)

    return left_valid and right_valid