import threading
from . import Warcraftlogs


class CollectWlogsStats(threading.Thread):

    def __init__(self, player, difficulty):
        threading.Thread.__init__(self)
        self.player = player
        self.difficulty = difficulty


    def run(self):
        print("Collecting Data from Warcraftlogs ({},{})...".format(self.player.getDifficultyName(self.difficulty), self.player.role))
        self.player.get_Stats(self.difficulty)
