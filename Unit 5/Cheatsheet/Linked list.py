class Node:
    def __init__(self, val, next = None):
        self.value = val
        self.next = next

head = Node(5)
n1 = Node(6)
n2 = Node(8)
n3 = Node(9)

head.next = n1
n1.next = n2
n2.next = n3

current = head
while current:
    print(current.value)
    current = current.next

