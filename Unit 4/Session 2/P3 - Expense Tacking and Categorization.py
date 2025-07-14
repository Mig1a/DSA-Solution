"""
function 1 args,
1. a list of tuples - each with string representing catagories of expenses
and float amount of expenses

Function have to process the total expense for each catagories

return the total expense for each expense and the max expense catagory

Create a dict
iterate through the expenses, if catagory isnt in the list add it and add the expense as a value
if the catagory is already in the dict add its value
sort the dict
return the sorted list and the lat key
"""

def calculate_expenses(expenses):
    cont = {}

    for i in expenses:
        if i[0] in cont:
            cont[i[0]] += i[1]
        else:
            cont[i[0]] = i[1]
    m = max(cont, key=cont.get)
    return (cont,m)
expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses))

expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))

