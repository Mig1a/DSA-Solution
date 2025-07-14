# function takes 2 args, 1 list of int representing event id, and 2 a single int
#return boolean by checking the event id's similarity and their diffrernces of their time point
#and the given int

#var left and right
#while loop untill left and right are equal, using the left and right check for similar events,
#if similar events detected check they are equal to the given int

def detect_temporal_anomaly(time_points, k):
    seen = {}
    for i,j in enumerate(time_points):
        if j in seen and i - seen[j] == k:
            return True
        seen[j] = i
    return False

time_points1 = [1, 2, 3, 1]
k1 = 3

time_points2 = [1, 0, 1, 1]
k2 = 1

time_points3 = [1, 2, 3, 1, 2, 3]
k3 = 2

print(detect_temporal_anomaly(time_points1, k1))
print(detect_temporal_anomaly(time_points2, k2))
print(detect_temporal_anomaly(time_points3, k3))


