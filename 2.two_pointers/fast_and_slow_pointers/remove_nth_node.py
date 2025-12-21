class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):
    dummy_head = Node(val=None, next=head)

    slow = fast = dummy_head

    for i in range(n):
        if fast.next:
            fast = fast.next
        else:
            return dummy_head.next


    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy_head.next

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None:
        return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)


def format_list(node):
    if node is None:
        return
    yield str(node.val)
    yield from format_list(node.next)


if __name__ == "__main__":
    head = build_list(iter(input().split()), int)
    n = int(input())
    res = remove_nth_from_end(head, n)
    print(" ".join(format_list(res)))