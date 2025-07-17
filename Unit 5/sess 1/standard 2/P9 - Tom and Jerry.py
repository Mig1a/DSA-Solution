class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

cat = Node('Tom')
mouse = Node('Jerry')

cat.next = mouse

print(cat.value)
print(cat.next)
print(cat.next.value)
print(mouse.value)
print(mouse.next)

dog = Node('Spike')

dog.next = cat

print(dog.value)
print(dog.next)
print(dog.next.value)
print(cat.next)
print(cat.next.value)
print(mouse.next)

def chase_list(head):
    current = head
    while current:
        print(current.value, end='')
        if current.next:
            print(" chases ", end='')
        current = current.next
    print()  # for newline at the end


og = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print(chase_list(dog))
