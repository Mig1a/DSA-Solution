"""
Function takes 2 args,
1, a list of int representing time each task takes
2. an int representing time slot available

function have to process pairs that fits in the time slot
meaning task[i] + task[j] = time slot return True in this case and false
if there is no a pair of task that fits in time slot

create an empty list
iterate through the list of int
if the difference between an item and the slot is in the list return true
else add the item to the list
return false
"""

def find_task_pair(task_times, available_time):
    cont = []
    for i in task_times:
        if available_time - i in cont:
            return True
        else:
            cont.append(i)
    return False

task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))