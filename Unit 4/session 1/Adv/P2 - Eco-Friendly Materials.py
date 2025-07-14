#function takes 1 arg, a list of brands as a dict with names and their list of materials
#let the function process the material and count each material from every brand

#create a dict to store the material and thier counts
#iterate through the list and a second loop in the material list
#check if the material is in the dict and assign or increment based on that

#if material list is empty

def count_material_usage(brands):
    res = {}
    for brand in brands:
        for material in brand['materials']:
            if material in res:
                res[material] += 1
            else:
                res[material] = 1
    return res
brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(count_material_usage(brands))
print(count_material_usage(brands_2))
print(count_material_usage(brands_3))