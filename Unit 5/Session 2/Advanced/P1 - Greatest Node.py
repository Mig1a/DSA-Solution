class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_max(head):
    current = head
    result = float('-inf')
    while current:
        result = max(result,current.value)
        current = current.next
    return result


def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None

    current = head
    while current.next.next:
        current = current.next

    current.next = None
    return head
def delete_dupes(head):
    tem_head = Node('temp')
    tem_head.next = head

    pre = tem_head
    current = head

    while current.next.next:
        if current.value == current.next.value:
            pre.next = current.next.next

        pre = current
        current = current.next
    return tem_head.next


def has_cycle(head):
    if not head:
        return False

    slow = head  # Starts at the head
    fast = head  # Also starts at the head

    while fast and fast.next:
        slow = slow.next  # Move slow pointer by one
        fast = fast.next.next  # Move fast pointer by two
        
        if slow == fast:  # If they meet, there's a cycle
            return True

    return False

head1 = Node(5, Node(6, Node(7, Node(8))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_max(head1))

head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
print(find_max(head2))

head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
print(print_linked_list(remove_tail(head)))

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print(print_linked_list(delete_dupes(head)))

peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# Toad.next = Luigi
peach.next.next.next = peach.next

print(has_cycle(peach))