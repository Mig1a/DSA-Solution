class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []

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