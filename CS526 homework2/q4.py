class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

def sum_three_middle(head):
    
    n, temp = 0, head
    while temp:
        n += 1
        temp = temp.next
    

    mid = n // 2
    temp = head
    for _ in range(mid - 1):
        temp = temp.next
    

    return temp.value + temp.next.value + temp.next.next.value


nodes = [Node(v) for v in [2, 4, 8, 10, 15, 29, 41]]
for i in range(len(nodes)-1):
    nodes[i].next, nodes[i+1].prev = nodes[i+1], nodes[i]
head = nodes[0]

print(sum_three_middle(head))  
