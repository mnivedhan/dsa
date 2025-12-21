class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def find_lca(bst: Node, p: int, q: int):
    if not bst:
        return None

    if p < bst.value and q < bst.value:
        return find_lca(bst.left, p, q)
    elif p > bst.value and q > bst.vaue:
        return find_lca(bst.right, p, q)
    else:
        return bst.value

if __name__ == '__main__':
    node_3 = Node(3)
    node_5 = Node(5)
    node_4 = Node(4, node_3, node_5)
    node_0 = Node(0)
    node_2 = Node(2, node_0, node_4)
    node_7 = Node(7)
    node_9 = Node(9)
    node_8 = Node(8, node_7, node_9)
    node_6 = Node(6, node_2, node_8)
    print(find_lca(node_6, 2, 4))







