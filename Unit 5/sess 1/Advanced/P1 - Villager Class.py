class Villager:
    def __init__(self,name,species,personality,catchphrase,neighbor = None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.neighbor = neighbor
        self.furniture = []

    #Problem 2: Add Furniture
    def add_item(self,item_name):
        valid = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu","cacao tree"]
        if item_name in valid:
            self.furniture.append(item_name)

#Problem 3: Group by Personality
def of_personality_type(townies, personality_type):
    cont = []
    for i in townies:
        if i.personality == personality_type:
            cont.append(i.name)
    return cont

#Problem 4: Telephone
def message_received(start_villager, target_villager):
    current = start_villager
    cont = set()
    while current.neighbor:
        cont.add(current.name)
        current = current.neighbor
    if current.name == target_villager.name or target_villager.name in cont:
        return True
    else:
        return False


isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))