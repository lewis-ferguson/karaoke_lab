import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room(1)
        self.guest = Guest("Lewis", 500)
        self.song = Song("Heaven and Hell", "Black Sabbath")
        
        
    
    def test_room_has_list_of_guests(self):
        self.assertEqual([],self.room.guests)
    
    def test_room_check_in(self):
        self.room.check_in(self.guest) # adds a guest to an empty list
        self.assertTrue(self.guest in self.room.guests)
    
    def test_room_check_out(self):
        self.room.check_in(self.guest) #adding a guest to the list, as the list starts empty
        self.room.check_out(self.guest)
        print(self.room.guests) #using print to debug as I was having issues
        self.assertFalse(self.guest in self.room.guests)
        
    def test_add_song(self):
        self.room.add_song(self.song) #adds a song to an empty list 
        self.assertTrue(self.song in self.room.songs)   #searches through the list to find the object
        
    def test_guest_limit(self):
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest) #Adding 4 guests as it should return "No space left, sorry!" on the 5th entry on the line below.
        self.assertEqual("No space left, sorry!", self.room.check_in(self.guest))
     
    def test_pay_entry_fee(self):
        self.room.pay_entry_fee(self.guest) #call the method and then pass the value of the guests wallet which is changed after the method is run
        self.assertEqual(495,self.guest.wallet)
        