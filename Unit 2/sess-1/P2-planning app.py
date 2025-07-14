#function takes 2 arguments of a string-artist name and
# a dictionary- artists festival performance info
# return the performance info of a specific artist
#if artist is not in the dictionary return not found

# if artist not in festival_schedule - return {"message": "Artist not found"}
# return festival_schedule[artist]

def get_artist_info(artist, festival_schedule):
    if artist not in festival_schedule:
        return {"message": "Artist not found"}
    return festival_schedule[artist]

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule))
print(get_artist_info("Taylor Swift", festival_schedule))