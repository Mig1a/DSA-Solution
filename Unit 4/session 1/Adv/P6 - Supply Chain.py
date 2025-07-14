"""
Time Complexity: O(n log n)
Sorting takes O(n log n) where n is the number of supplies.

List comprehension to extract names is O(n).

Total: O(n log n)

Space Complexity: O(n)
sorted_supplies creates a new list → O(n)

Output list of names → O(n)
"""
def process_supplies(supplies):
    # Sort by priority (descending), keep original order for ties
    sorted_supplies = sorted(supplies, key=lambda x: -x[1])
    return [name for name, _ in sorted_supplies]
supplies = [("Organic Cotton", 3), ("Recycled Polyester", 2), ("Bamboo", 4), ("Hemp", 1)]
supplies_2 = [("Linen", 2), ("Recycled Wool", 5), ("Tencel", 3), ("Organic Cotton", 4)]
supplies_3 = [("Linen", 3), ("Hemp", 2), ("Recycled Polyester", 5), ("Bamboo", 1)]

print(process_supplies(supplies))
print(process_supplies(supplies_2))
print(process_supplies(supplies_3))