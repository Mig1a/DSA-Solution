import math
class Node:
    def __init__(self,value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

#Problem 6: Got One!
def catch_fish(head):
    current = head
    if current == None:
        return "Aw! Better luck next time!"
    while current:
        print(f'I caught a {current.value}!')
        current = current.next

#Problem 7: Fishing Probability
def fish_chances(head, fish_name):
    current = head
    cont = 0
    match = 0
    while current:
        if current.value == fish_name:
            match += 1
        cont += 1
        current = current.next
    if match == 0:
        return 0.00
    pr = match / cont
    return math.floor(pr * 100) / 100
def restock(head, new_fish):
    current = head
    new = Node(new_fish)
    while current.next:
        current = current.next
    current.next = new
    return head




kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

print(print_linked_list(kk_slider))

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print(print_linked_list(fish_list))
print(print_linked_list(catch_fish(fish_list)))
print(catch_fish(empty_list))

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print(fish_chances(fish_list, "Dace"))
print(fish_chances(fish_list, "Rainbow Trout"))

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print(print_linked_list(restock(fish_list, "Rainbow Trout")))

