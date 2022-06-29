from somegame.service import Service
from somegame.actor import Hider
from somegame.action import Seeker


class Director:
    def __init__(self):
        self._is_playing = True
        self._hider = Hider()
        self._service = Service()
        self._seeker = Seeker()
        
        
    def start_game(self):
        while self._is_playing:
            self._inputs()
            self._outputs()
            self._updates()
            
    def _inputs(self):
        new_location = self._service.read_number("\nEnter a number (1-1000): ")
        self._seeker.move_location(new_location)
        #updated after looking at example
    def _updates(self):
        self._hider.watch_seeker(self._seeker)
        
    def _outputs(self):
        hint = self._hider.get_hint()
        self._service.write_text(hint)
        if self._hider.is_found():
            self._is_playing = False