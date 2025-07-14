#function takes 1 arg, of 2d array, i= str,str-dig,str-time
def display_time_portal_usage(usage_records):
    dis = {'portal':[]}
    po = [['Portal']]
    for i in usage_records:
        if i[-1] not in dis['portal']:
            dis['portal'].append(i[-1])
        if int(i[1]) not in dis:
            dis[int(i[1])] = [1]
            po.append([i[1]])
        else:
            dis[int(i[1])] += 1
    so = dict(sorted(dis.items(),key=lambda x:x[0]))
    print(po)




usage_records1 = [["David","3","10:00"],
                  ["Corina","10","10:15"],
                  ["David","3","10:30"],
                  ["Carla","5","11:00"],
                  ["Carla","5","10:00"],
                  ["Rous","3","10:00"]]
usage_records2 = [["James","12","11:00"],
                  ["Ratesh","12","11:00"],
                  ["Amadeus","12","11:00"],
                  ["Adam","1","09:00"],
                  ["Brianna","1","09:00"]]
usage_records3 = [["Laura","2","08:00"],
                  ["Jhon","2","08:15"],
                  ["Melissa","2","08:30"]]

print(display_time_portal_usage(usage_records1))
print(display_time_portal_usage(usage_records2))
print(display_time_portal_usage(usage_records3))



