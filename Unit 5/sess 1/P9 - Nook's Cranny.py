class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


tom_nook = Node('Tom nook')
timy = Node('timmy')
tommy = Node('Tommy')
saharah = Node('sarah')

tom_nook.next = timy
timy.next = tommy
tommy.next = saharah

def print_list(a):
    current = a
    while current:
        print(current.value,"-> ",end='')
        current = current.next

print(print_list(tom_nook))

