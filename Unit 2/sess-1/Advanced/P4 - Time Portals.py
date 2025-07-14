#function takes 2 args, one a list of digit str and a single str
#return the number strs that equals the destination when they are concatinated
# portal[i] + portal[j] == destination, concatination of i+j and j+i is considered different

#var count = 0
#nested loop, concatenate i+j and j+i if the concatination == destination
#add 1 to count
#return count

def num_of_time_portals(portals, destination):
    count = 0
    for i in range(len(portals)):
        for j in range(i,len(portals)-1):
            if portals[i] + portals[j+1] == destination:
                count += 1
            if portals[j+1] + portals[i] == destination:
                count += 1
    return count

portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))