class Node:
    def __init__(self, val, next = None):
        self.value = val
        self.next = next
class Linkedlist:
    def __init__(self, head=None):
        self.head = head

    def add_first(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node


    def append(self,val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def length(self):
        current = self.head
        length = 0

        while current:
            length += 1
            current = current.next

        return length

    def get_at_index(self, index):
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.value
            current = current.next
            count += 1

        # If we exit the loop, index is out of range
        return None


ll = Linkedlist()
ll.add_first(5)
ll.append(9)
ll.add_first(100)
print(ll.length())
print(ll.get_at_index(0))