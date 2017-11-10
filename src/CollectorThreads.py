import threading
from . import Warcraftlogs


class CollectWlogsStats(threading.Thread):

    def __init__(self, player, difficulty, role):
        threading.Thread.__init__(self)
        self.player = player
        self.difficulty = difficulty
        self.role = role

    def run(self):
        print("Collecting Data from Warcraftlogs ({},{})...".format(self.player.getDifficultyName(self.difficulty), self.role))
        self.player.get_Stats(self.difficulty, self.role)
