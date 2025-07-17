class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

        # Problem 2: Greet Player
        def greet_player(self, player_name):
            return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

        # Problem 4: Set Character
        def set_catchphrase(self, new_catchphrase):
            if (
                    len(new_catchphrase) < 20
                    and all(c.isalpha() or c.isspace() for c in new_catchphrase)
            ):
                self.catchphrase = new_catchphrase
                return "Catchphrase updated"
            else:
                return "Invalid catchphrase"

        # Problem 5: Add Furniture
        def add_item(self, item_name):
            valid = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
            if item_name in valid:
                self.furniture.append(item_name)

        # Problem 6: Print Inventory
        def print_inventory(self):
            if not self.furniture:
                return 'Inventory empty'
            cont = {}
            for i in self.furniture:
                if i in cont:
                    cont[i] += 1
                else:
                    cont[i] = 1
            return cont

def of_personality_type(townies, personality_type):
    cont = []
    for i in townies:
        if i.personality == personality_type:
            cont.append(i.name)
    return cont

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))

#Problem 8: Telephone
def message_received(start_villager, target_villager):
    current = start_villager
    nei = set()
    while current:
        if target_villager == current:
            return True
        if current in nei:
            return False
        nei.add(current)
        current = current.neighbor
    return False




isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))


