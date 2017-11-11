#--------------------------------------------
# Imports
import sys
import argparse

from src.Warcraftlogs import Warcraftlogs
from src.HtmlGenerator import HtmlGen
from src.CollectorThreads import CollectWlogsStats
from src.BlizzardArsenal import BlizzStats
from settings import *

def main():

    if BLIZZARD_APIKEY == '':
        sys.stderr.write("Error: Please make sure the Blizzard-Apikey is set in settings.py!")
        sys.stderr.flush()
        exit(1)

    if WARCRAFTLOGS_APIKEY == '':
        sys.stderr.write("Error: Please make sure the Warcraftlogs-Apikey is set in settings.py!")
        sys.stderr.flush()
        exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("playername", help="Name of the player")
    parser.add_argument("server", help="Server name, e.g. Blackhand")
    parser.add_argument("--region", help="Region default is EU", choices=["EU", "US"], default="EU")
    parser.add_argument("--role", help="Which stat to check. e.g. damage done or healing", choices=["damage-done", "healing"], default="damage-done")
    args = parser.parse_args()

    #--------------------------------------------
    # Collecting Data
    #
    wlogs = Warcraftlogs(args.playername, args.server, args.region, args.role, WARCRAFTLOGS_APIKEY)

    collect_nhc = CollectWlogsStats(wlogs, 3)
    collect_hc = CollectWlogsStats(wlogs, 4)
    collect_my = CollectWlogsStats(wlogs, 5)

    collect_nhc.start()
    collect_hc.start()
    collect_my.start()

    blizz = BlizzStats(args.playername, args.server, args.region, BLIZZARD_APIKEY)

    collect_nhc.join()
    collect_hc.join()
    collect_my.join()
    print("...Done! (Warcraftlogs)")

    #--------------------------------------------
    # output
    outputs = [blizz.getCharinfoHtml(), wlogs.getHtml(), blizz.getPvpHtml(), blizz.getMplusHtml()]
    gen = HtmlGen( outputs, args.playername , args.server, args.region)
    gen.start()


if __name__ == "__main__":
   main()
