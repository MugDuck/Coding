import random as r

class Seeker:
    def __init__(self):
        self._location = r.randint(1, 1000)
        
    def get_location(self):
        return self._location
        
    def move_location(self, location):
        self._location = location