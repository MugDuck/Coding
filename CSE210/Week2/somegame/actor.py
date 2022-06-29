import random as r

class Hider:
    def __init__(self):
        self._location = r.randint(1, 1000)
        self._distance = [0, 0]
    
    def get_hint(self):
        hint = "You already typed this"
        if self._distance[-1] == 0:
            hint = "Found me!"
        elif self._distance[-1] > self._distance[-2]:
            hint = "Cold!"
        elif self._distance[-1] < self._distance[-2]:
            hint = "Warm!"
        return hint

    def is_found(self):
        return (self._distance[-1] == 0)
        
    def watch_seeker(self, seeker):
        distance = abs(self._location - seeker.get_location())
        self._distance.append(distance)