#function takes 1 argument of dictionary holding
#type of key ticket(str) and value sold(int)
#sum the value - total sold

#sum(ticket_sales.values)

def total_sales(ticket_sales):
    return sum(ticket_sales.values())
ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))