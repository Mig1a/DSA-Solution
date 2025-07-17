class Player():
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent

    def get_player(self):
        return f"{self.character} driving the {self.kart}"

    def set_character(self,name):
        valid = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong","Bowser"]
        if name in valid:
            self.character = name
            return "Character updated"
        else:
            return "Invalid character"

    def add_item(self,item_name):
        valid = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]
        if item_name in valid:
            self.items.append(item_name)

    def print_inventory(self):
        cont = {}
        if not self.items:
            return "Inventory empty"
        for i in self.items:
            if i in cont:
                cont[i] += 1
            else:
                cont[i] = 1
        return "Inventory: ", cont

def print_results(race_results):
    for i,k in enumerate(race_results):
        print(f'{i+1}. {k.character}')
    return

def get_rank(my_player):
    count = 0
    current = my_player
    while current:
        count += 1
        current = current.ahead
    return count



player_one = Player("Yoshi","Super Blooper")
print(player_one.character)
print(player_one.kart)
print(player_one.items)

player_two = Player("Bowser", "Pirahna Prowler")
print(player_two.get_player())

player_one.kart = "Dolphin Dasher"
print(player_one.kart)

player_three = Player("Donkey Kong", "Standard Kart")

print(player_three.set_character("Peach"))
print(player_three.character)
print(player_three.set_character("Baby Peach"))
print(player_three.character)


player_one = Player("Yoshi", "Dolphin Dasher")

print(player_one.items)

player_one.add_item("red shell")
print(player_one.items)

player_one.add_item("super star")
print(player_one.items)

player_one.add_item("super smash")
print(player_one.items)

player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

print(player_one.print_inventory())
print(player_two.print_inventory())


peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print(print_results(race_one))

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)
print(get_rank(luigi))
print(get_rank(peach))
print(get_rank(mario))
