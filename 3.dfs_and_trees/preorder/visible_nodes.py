class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def visible_nodes(node: Node):
   def dfs(node: Node, max_so_far):
        if not node:
               return 0

        total = 0

        if node.value >= max_so_far:
           total += 1

        total = total + dfs(node.left, max(node.value, max_so_far)) + dfs(node.right, max(node.value, max_so_far))

        return total

   return dfs(node, -1)


if __name__ == '__main__':
    node_2 = Node(2)
    node_3 = Node(3, Node(5))
    node_1 = Node(1, node_2, node_3)
    print(visible_nodes(node_1) - 1)