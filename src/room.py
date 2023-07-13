

class Room:
    
    def __init__(self, room_number):
        self.guests = []
        self.room_number = room_number
        self.songs = []
    
    def check_in(self, guest):
        self.guests.append(guest)
    
    def check_out(self,guest):
        self.guests.remove(guest)
        
    def add_song(self, song):
        self.songs.append(song)