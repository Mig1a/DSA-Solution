"""
function takes 2 args

1. a list of int, representing a list of time for a task
2. an int, representing the available time

function have to process and find the maximum number of tasks that can be completed
with in the available time frame

return an int

sort the list ascendigly
create a var to count
iterate through the list, and substract each item from the time limit,
if the item less than the time limit
return the count

"""

def max_tasks_within_time(tasks, time_limit):
    tasks.sort()
    count = 0
    for i in tasks:
        if i <= time_limit:
            time_limit -= i
            count += 1
        else:
            break
    return count
tasks = [5, 10, 7, 8]
time_limit = 20
print(max_tasks_within_time(tasks, time_limit))

tasks_2 = [2, 4, 6, 3, 1]
time_limit = 10
print(max_tasks_within_time(tasks_2, time_limit))

tasks_3 = [8, 5, 3, 2, 7]
time_limit = 15
print(max_tasks_within_time(tasks_3, time_limit))