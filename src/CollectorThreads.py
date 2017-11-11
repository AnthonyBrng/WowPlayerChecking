import threading
from . import Warcraftlogs


class CollectWlogsStats(threading.Thread):
    '''
        DESCRIPTION:    Provides a new thread collecting data from Warcraftlogs for
                        a specific raid difficulty.
        INPUT:          wlogs - Warcraftlogs-Object
                        difficulty - integer
    '''
    def __init__(self, wlogs, difficulty):
        threading.Thread.__init__(self)
        self.wlogs = wlogs
        self.difficulty = difficulty


    def run(self):
        '''
        DESCRIPTION:    Starts a new Thread collecting data for a specific raid
                        difficulty.
        '''
        print("Collecting Data from Warcraftlogs ({},{})...".format(self.wlogs.getDifficultyName(self.difficulty), self.wlogs.role))
        self.wlogs.get_Stats(self.difficulty)
