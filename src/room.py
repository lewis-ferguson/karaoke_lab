

class Room:
    
    def __init__(self, room_number):
        self.guests = []
        self.room_number = room_number
        self.songs = []
        self.entry_fee = 5
    
    def check_in(self, guest):
        if len(self.guests) > 4:
            return("No space left, sorry!")
        else:
            self.guests.append(guest)
    
    def check_out(self,guest):
        self.guests.remove(guest)
        
    def add_song(self, song):
        self.songs.append(song)
        
    def pay_entry_fee(self, guest):
        guest.wallet -= self.entry_fee