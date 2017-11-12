
import sys, time, threading
from . import Warcraftlogs
from .stdio import debugPrint, DEBUG

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
        debugPrint("Collecting Data from Warcraftlogs ({},{})...".format(self.wlogs.getDifficultyName(self.difficulty), self.wlogs.role))
        self.wlogs.get_Stats(self.difficulty)


class WorkingThread(threading.Thread):
    '''
    DESCRIPTION     Simple thread to just display, that the program is running.
                    Writing to stdout
    INPUT:          None
    OUTPUT:         None
    '''
    def __init__(self):
        threading.Thread.__init__(self)
        if not DEBUG:
            sys.stdout.write("Checking")
            self.running = True


    def run(self):
        '''
        DECRIPTION:     prints every second a "."(dot) on stdout.
        INPUT:          None
        OUTPUT:         None
        '''
        while self.running and not DEBUG:
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(1)

    def stop(self):
        '''
        DESCRIPTION:    Stops the thread
        INPUT:          None
        OUTPUT:         None
        '''
        self.running = False
        sys.stdout.write("done!\n")
        sys.stdout.flush()
