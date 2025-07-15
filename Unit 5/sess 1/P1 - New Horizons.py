class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    #Problem 2: Greet Player
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    #Problem 4: Set Character
    def set_catchphrase(self, new_catchphrase):
        if (
            len(new_catchphrase) < 20
            and all(c.isalpha() or c.isspace() for c in new_catchphrase)
        ):
            self.catchphrase = new_catchphrase
            return "Catchphrase updated"
        else:
            return "Invalid catchphrase"
    #Problem 5: Add Furniture
    def add_item(self, item_name):
        valid = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in valid:
            self.furniture.append(item_name)

    #Problem 6: Print Inventory
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
    #Problem 7: Group by Personality


apollo = Villager('Apollo','Eagle','Pah')
print(apollo.name)
print(apollo.species)
print(apollo.catchphrase)
print(apollo.furniture)
print(apollo.greet_player('pollo'))

bones = Villager('Bones','Dog','yip yip')
print(bones.greet_player('Million'))


# Problem 3: Update Catchphrase
bones.catchphrase = "ruff it up"
print(bones.greet_player("Samia"))


#Problem 4: Set Character

alice = Villager("Alice", "Koala", "guvnor")

print(alice.set_catchphrase("sweet dreams"))
print(alice.catchphrase)
print(alice.set_catchphrase("#?!"))
print(alice.catchphrase)

#Problem 5: Add Furniture
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

#Problem 6: Print Inventory
alice = Villager("Alice", "Koala", "guvnor")

print(alice.print_inventory())

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
print(alice.print_inventory())
