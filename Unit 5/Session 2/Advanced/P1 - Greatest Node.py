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

#Problem 5: Remove Nth Node From End of List
def remove_nth_from_end(head, n):
    temp = Node('temp')
    temp.next = head

    pre = temp
    current = head
    count = 0



    while current and count < n:
        pre = current
        current = current.next
        count += 1

    if count == n:
        if current:
            pre.next = current.next
        else:
            pre.next = None

    return temp.next

def reverse_first_k(head, k):
    if not head or k <= 0:
        return head

    prev = None
    # Reset counters
    current = head
    count = 0

    # Reverse first k nodes
    while count < k and current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1

    # Connect the end of reversed list to the rest
    head.next = current

    # Return new head (prev is now the head of reversed part)
    return prev




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

head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
head2 = Node("Rainbow Trout", Node("Ray"))
head3 = Node("Rainbow Stag")


print(print_linked_list(remove_nth_from_end(head1, 0)))
print(print_linked_list(remove_nth_from_end(head2, 1)))
print(print_linked_list(remove_nth_from_end(head3, 0)))

head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))

print_linked_list(reverse_first_k(head, 3))