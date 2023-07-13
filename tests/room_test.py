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
        self.room.check_in(self.guest)
        self.assertTrue(self.guest in self.room.guests)
    
    def test_room_check_out(self):
        self.room.check_in(self.guest)
        self.assertTrue(self.guest in self.room.guests)
        self.room.check_out(self.guest)
        print(self.room.guests)
        self.assertFalse(self.guest in self.room.guests)
        
    def test_add_song(self):
        self.room.add_song(self.song)
        self.assertTrue(self.song in self.room.songs)    