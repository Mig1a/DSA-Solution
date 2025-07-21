class SongNode:
	def __init__(self, song, next=None):
		self.song = song
		self.next = next

def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()
third_song = SongNode("Bad Romance")
second_song = SongNode("Party Rock Anthem",third_song)
first_song = SongNode("Uptown Funk",second_song)

print(print_linked_list(first_song))

