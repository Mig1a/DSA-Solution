#function takes two args, both holds artifacts,
# return artifacts present in bothe lists

#a list holding the result
# iterate the first arg and check each item is available in the seond arg
# if available appended it to the result list

def find_common_artifacts(artifacts1, artifacts2):
    res = []

    for i in artifacts1:
        if i in artifacts2:
            res.append(i)
    return res
artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))