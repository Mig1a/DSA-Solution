"""
function takes 1 arg,

1. a list of tuple - representing a place and a time stamp

process the frequency of the places

and return the most frequently visited place if there is a tie, return the latest based on the time

Create a dict
iterate through the list and add their frequency to the dict
and update the time stamp


"""
from datetime import datetime
def most_popular_destination(visits):
    cont = {}

    for i in visits:
        place = i[0]
        visit_date = datetime.strptime(i[1], "%Y-%m-%d").date()

        if place in cont:
            cont[place][0] += 1  # Increment count
            # Update latest date only if this one is more recent
            if visit_date > cont[place][1]:
                cont[place][1] = visit_date
        else:
            cont[place] = [1, visit_date]  # [count, latest_date]
    most = sorted(cont.items(), key=lambda x: (-x[1][0], -x[1][1].toordinal()))
    return (most[0][0],most[0][1][0])
visits = [("Paris", "2024-07-15"), ("Tokyo", "2024-08-01"), ("Paris", "2024-08-05"), ("New York", "2024-08-10"), ("Tokyo", "2024-08-15"), ("Paris", "2024-08-20")]
print(most_popular_destination(visits))

visits_2 = [("London", "2024-06-01"), ("Berlin", "2024-06-15"), ("London", "2024-07-01"), ("Berlin", "2024-07-10"), ("London", "2024-07-15")]
print(most_popular_destination(visits_2))

visits_3 = [("Sydney", "2024-05-01"), ("Dubai", "2024-05-15"), ("Sydney", "2024-05-20"), ("Dubai", "2024-06-01"), ("Dubai", "2024-06-15")]
print(most_popular_destination(visits_3))