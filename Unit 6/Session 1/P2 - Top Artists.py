class SongNode:
    def __init__(self,song,artist,next = None):
        self.song = song
        self.artist = artist
        self.next = next
# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()
def get_artist_frequency(playlist):
    current = playlist

    cont = {}

    while current:
        if current.artist in cont:
            cont[current.artist] += 1
        else:
            cont[current.artist] = 1
        current = current.next
    return cont

playlist = SongNode("Saturn", "SZA",
                SongNode("Who", "Jimin",
                        SongNode("Espresso", "Sabrina Carpenter",
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))