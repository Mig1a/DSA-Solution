#function takes 1 arg, a list of int, rep a height of building
#when an item is equal or greater than another item
#build the sky scraper
#if less than the current item crate new

def build_skyscrapers(floors):
    top = floors[0]
    count = 1

    for i in floors[1:]:
        if top >= i:
            top = i
        else:
            count += 1
            top = i
    return count
print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9]))
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2]))