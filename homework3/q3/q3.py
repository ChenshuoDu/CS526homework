import sys

# Reverse stack implemented as array
def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    top = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(top)

def reverse_stack_array(stack):
    if not stack:
        return
    top = stack.pop()
    reverse_stack_array(stack)
    insert_at_bottom(stack, top)

# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linkedlist(head):
    if head is None or head.next is None:
        return head
    rest = reverse_linkedlist(head.next)
    head.next.next = head
    head.next = None
    return rest

# Doubly Linked List Node
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverse_doubly_linkedlist(head):
    if head is None:
        return None
    temp = head.next
    head.next = head.prev
    head.prev = temp
    if head.prev is None:
        return head
    return reverse_doubly_linkedlist(head.prev)

def main():
    if len(sys.argv) < 2:
        print("Usage: python reverse_stack.py <input_file>")
        return

    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        data = [int(x) for x in f.read().split(",")]

    stack = data[:]
    reverse_stack_array(stack)
    print("Reversed array stack:", stack)

if __name__ == "__main__":
    main()
