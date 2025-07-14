def find_smallest_gap(work_sessions):
    min_ses = float('inf')
    for i in range(len(work_sessions)-1):
        end = (work_sessions[i][1] // 100) * 60 + (work_sessions[i][1] % 100)
        start = (work_sessions[i + 1][0] // 100) * 60 + (work_sessions[i + 1][0] % 100)

        if start - end < min_ses:
            min_ses = start - end
    return min_ses

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))

