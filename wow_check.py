#--------------------------------------------
# Imports
from src.Warcraftlogs import Warcraftlogs
from src.HtmlGenerator import HtmlGen
from src.CollectorThreads import CollectWlogsStats

player_name = 'Horscanigun'
player_server = 'Blackhand'
player_region = 'EU'
api_key = '6bd918e14d71db254e0603d4bab015fe'

#--------------------------------------------
# Warcraftlogs
wlogs = Warcraftlogs(player_name, player_server, player_region, api_key)

collect_nhc = CollectWlogsStats(wlogs, 3, "damage-done")
collect_hc = CollectWlogsStats(wlogs, 4, "damage-done")
collect_my = CollectWlogsStats(wlogs, 5, "damage-done")

collect_nhc.start()
collect_hc.start()
collect_my.start()

collect_nhc.join()
collect_hc.join()
collect_my.join()
print("...Done! (Warcraftlogs)")

#--------------------------------------------
# Wowprogress



#--------------------------------------------
# output
outputs = [wlogs.getHtml()]
gen = HtmlGen( outputs, player_name, player_server, player_region)
gen.start()
